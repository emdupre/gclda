# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 et:
"""
Tests for GC-LDA dataset module.
"""
import sys
from shutil import rmtree
from os import remove
from os.path import join, isfile
try:
    # 2.7
    from StringIO import StringIO
except ImportError:
    # 3+
    from io import StringIO

import neurosynth
from gclda.dataset import Dataset
from gclda.tests.utils import get_test_data_path


def test_import_from_counts():
    """Ensure that Dataset files can be generated using counts file.
    """
    from gclda.dataset import import_neurosynth
    counts_file = join(get_test_data_path(), 'feature_counts.txt')
    ns_dset_file = join(get_test_data_path(), 'neurosynth_dataset.pkl')
    temp_dir = join(get_test_data_path(), 'temp')

    ns_dset = neurosynth.Dataset.load(ns_dset_file)
    import_neurosynth(ns_dset, 'temp', out_dir=get_test_data_path(),
                      counts_file=counts_file)
    files_found = [isfile(join(temp_dir, 'pmids.txt')),
                   isfile(join(temp_dir, 'peak_indices.txt')),
                   isfile(join(temp_dir, 'word_labels.txt')),
                   isfile(join(temp_dir, 'word_indices.txt'))]
    assert all(files_found)

    # Perform cleanup
    rmtree(temp_dir)


def test_import_from_abstracts():
    """Ensure that Dataset files can be generated using abstracts file.
    """
    from gclda.dataset import import_neurosynth
    abstracts_file = join(get_test_data_path(), 'abstracts.csv')
    ns_dset_file = join(get_test_data_path(), 'neurosynth_dataset.pkl')
    temp_dir = join(get_test_data_path(), 'temp')

    ns_dset = neurosynth.Dataset.load(ns_dset_file)
    import_neurosynth(ns_dset, temp_dir, out_dir=get_test_data_path(),
                      abstracts_file=abstracts_file)
    files_found = [isfile(join(temp_dir, 'pmids.txt')),
                   isfile(join(temp_dir, 'peak_indices.txt')),
                   isfile(join(temp_dir, 'word_labels.txt')),
                   isfile(join(temp_dir, 'word_indices.txt'))]
    assert all(files_found)

    # Perform cleanup
    rmtree(temp_dir)


def test_import_from_email():
    """Ensure that Dataset files can be generated using email.
    """
    from gclda.dataset import import_neurosynth
    email = 'tsalo006@fiu.edu'
    ns_dset_file = join(get_test_data_path(), 'neurosynth_dataset.pkl')
    temp_dir = join(get_test_data_path(), 'temp')

    ns_dset = neurosynth.Dataset.load(ns_dset_file)
    import_neurosynth(ns_dset, 'temp', out_dir=get_test_data_path(),
                      email=email)
    files_found = [isfile(join(temp_dir, 'pmids.txt')),
                   isfile(join(temp_dir, 'peak_indices.txt')),
                   isfile(join(temp_dir, 'word_labels.txt')),
                   isfile(join(temp_dir, 'word_indices.txt'))]
    assert all(files_found)

    # Perform cleanup
    rmtree(temp_dir)


def test_init():
    """Smoke test for Dataset class.
    """
    dataset_dir = get_test_data_path()
    dset = Dataset('dataset_files', dataset_dir)
    assert isinstance(dset, Dataset)


def test_load_dataset():
    """Test gclda.dataset.Dataset.load.
    """
    dataset_file = join(get_test_data_path(), 'gclda_dataset.pkl')
    dset = Dataset.load(dataset_file)
    assert isinstance(dset, Dataset)


def test_load_dataset2():
    """Test gclda.dataset.Dataset.load with gzipped file.
    """
    dataset_file = join(get_test_data_path(), 'gclda_dataset.pklz')
    dset = Dataset.load(dataset_file)
    assert isinstance(dset, Dataset)


def test_save_dataset():
    """Test gclda.dataset.Dataset.save.
    """
    dataset_file = join(get_test_data_path(), 'gclda_dataset.pkl')
    temp_file = join(get_test_data_path(), 'temp.pkl')
    dset = Dataset.load(dataset_file)
    dset.save(temp_file)
    file_found = isfile(temp_file)
    assert file_found

    # Perform cleanup
    remove(temp_file)


def test_save_dataset2():
    """Test gclda.dataset.Dataset.save with gzipped file.
    """
    dataset_file = join(get_test_data_path(), 'gclda_dataset.pklz')
    temp_file = join(get_test_data_path(), 'temp.pklz')
    dset = Dataset.load(dataset_file)
    dset.save(temp_file)
    file_found = isfile(temp_file)
    assert file_found

    # Perform cleanup
    remove(temp_file)


def test_display_dataset_summary():
    """Prints dataset information to the console.
    """
    dataset_file = join(get_test_data_path(), 'gclda_dataset.pkl')
    dset = Dataset.load(dataset_file)

    captured_output = StringIO()  # Create StringIO object
    sys.stdout = captured_output  #  and redirect stdout.
    dset.display_dataset_summary()  # Call unchanged function.
    sys.stdout = sys.__stdout__  # Reset redirect.

    assert len(captured_output.getvalue()) > 0


def test_view_word_labels():
    """Prints dataset information to the console.
    """
    dataset_file = join(get_test_data_path(), 'gclda_dataset.pkl')
    dset = Dataset.load(dataset_file)

    captured_output = StringIO()  # Create StringIO object
    sys.stdout = captured_output  #  and redirect stdout.
    dset.view_word_labels(n_word_labels=5)  # Call unchanged function.
    sys.stdout = sys.__stdout__  # Reset redirect.

    assert len(captured_output.getvalue()) > 0


def test_view_doc_labels():
    """Prints dataset information to the console.
    """
    dataset_file = join(get_test_data_path(), 'gclda_dataset.pkl')
    dset = Dataset.load(dataset_file)

    captured_output = StringIO()  # Create StringIO object
    sys.stdout = captured_output  #  and redirect stdout.
    dset.view_doc_labels(n_pmids=10)  # Call unchanged function.
    sys.stdout = sys.__stdout__  # Reset redirect.

    assert len(captured_output.getvalue()) > 0


def test_view_word_indices():
    """Prints dataset information to the console.
    """
    dataset_file = join(get_test_data_path(), 'gclda_dataset.pkl')
    dset = Dataset.load(dataset_file)

    captured_output = StringIO()  # Create StringIO object
    sys.stdout = captured_output  #  and redirect stdout.
    dset.view_word_indices(n_word_indices=5)  # Call unchanged function.
    sys.stdout = sys.__stdout__  # Reset redirect.

    assert len(captured_output.getvalue()) > 0


def test_view_peak_indices():
    """Prints dataset information to the console.
    """
    dataset_file = join(get_test_data_path(), 'gclda_dataset.pkl')
    dset = Dataset.load(dataset_file)

    captured_output = StringIO()  # Create StringIO object
    sys.stdout = captured_output  #  and redirect stdout.
    dset.view_peak_indices(n_peak_indices=5)  # Call unchanged function.
    sys.stdout = sys.__stdout__  # Reset redirect.

    assert len(captured_output.getvalue()) > 0
