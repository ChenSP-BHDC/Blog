@echo on

set BlogHOME=C:\www\Blogs

cd %BlogHOME%
pelican content
cd %BlogHOME%\output
python -m pelican.server
:quit
 pause