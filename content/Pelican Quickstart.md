Title: Pelican Quickstart  
Date: 2014-10-24 10:11  
Category:Pelican  
Tags: python,pelican,markdown 

####安装Pelican

`pip install pelican markdown`


####创建项目

`mkdir -p ~/projects/yoursite`
`cd ~/projects/yoursite`
`pelican-quickstart`


####发表文章

	Title: Pelican Quickstart  
	Date: 2014-10-24 10:11  
	Category:博客系统  
	Tags: python,pelican,markdown  

	下面是文章的正文

保存到~/projects/yoursite/content/pelican_quickstart.md

####生成网页

`pelican content`


生成的网页在~/projects/yoursite/output

####预览网页

`cd ~/projects/yoursite/output`

####END
