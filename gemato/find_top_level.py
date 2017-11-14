# gemato: Top-level Manifest finding routine
# vim:fileencoding=utf-8
# (c) 2017 Michał Górny
# Licensed under the terms of 2-clause BSD license

import errno
import os
import os.path

import gemato.compression
import gemato.manifest


def find_top_level_manifest(path='.', allow_compressed=False):
    """
    Find top-level Manifest file that covers @path (defaults
    to the current directory). Returns the path to the Manifest
    or None.

    If @allow_compressed is true, the function allows the top-level
    Manifest to be compressed and opens all compressed files *without*
    verifying them first. It is false by default to prevent zip bombs
    and other decompression attacks.
    """

    cur_path = path
    last_found = None
    original_dev = None
    m = gemato.manifest.ManifestFile()

    root_st = os.stat('/')

    manifest_filenames = ('Manifest',)
    if allow_compressed:
        manifest_filenames = list(gemato.compression
                .get_potential_compressed_names('Manifest'))

    while True:
        st = os.stat(cur_path)

        # verify that we are not crossing device boundaries
        if original_dev is None:
            original_dev = st.st_dev
        elif original_dev != st.st_dev:
            break

        m_path = os.path.join(cur_path, 'Manifest')
        for m_name in manifest_filenames:
            m_path = os.path.join(cur_path, m_name)
            try:
                # note: this is safe for allow_compressed=False
                # since it detects compression by filename suffix
                with (gemato.compression
                        .open_potentially_compressed_path(m_path, 'r',
                            encoding='utf8')) as f:
                    fst = os.fstat(f.fileno())
                    if fst.st_dev != original_dev:
                        return last_found

                    m.load(f, verify_openpgp=False)
            except IOError as e:
                if e.errno != errno.ENOENT:
                    raise
            else:
                # check if the initial path is ignored
                relpath = os.path.relpath(path, cur_path)
                if relpath == '.':
                    relpath = ''
                fe = m.find_path_entry(relpath)
                if fe is not None and fe.tag == 'IGNORE':
                    return last_found

                last_found = m_path
                break

        # check if we reached root directory
        if st.st_dev == root_st.st_dev and st.st_ino == root_st.st_ino:
            break

        # try the parent directory
        cur_path = os.path.join(cur_path, '..')

    return last_found
