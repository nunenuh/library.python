import shutil
import os

#copy and paste operation
base_path = os.getcwd()
srcdir = os.path.join(base_path, 'dir1')
srcfile = os.path.join(srcdir, 'sample.txt')
dstdir = os.path.join(base_path, 'dir2')
res = shutil.copy(srcfile, dstdir)
print(res)

#copy directory with all of the file and directory inside of it
base_path = os.getcwd()
srcdir = os.path.join(base_path, 'testdir')
dstdir = os.path.join(base_path, 'treecopy')
res = shutil.copytree(srcdir, dstdir)
print(res)


# delete directory with all of its file and directory inside of it
res = shutil.rmtree(dstdir)
print(res)

#moving directory and all of its files and directory
base_path = os.getcwd()
srcdir = os.path.join(base_path, 'treecopy')
dstdir = os.path.join(base_path, 'dir1','treecopy')
shutil.move(srcdir, dstdir)


# compressing directory with shutil
base_path = os.getcwd()
root_dir = os.path.join(base_path, 'dir1','treecopy')
archived_dir = os.path.join(base_path, 'compressed')
shutil.make_archive(archived_dir, 'zip', root_dir)
shutil.make_archive(archived_dir, 'gztar', root_dir)


# unpacking compressed file with shutil
base_path = os.getcwd()
compressed_file = os.path.join(base_path, 'compressed.tar.gz')
dstdir_unpacked = os.path.join(base_path, 'extracted_tar_gz')
shutil.unpack_archive(compressed_file,dstdir_unpacked, 'gztar')
