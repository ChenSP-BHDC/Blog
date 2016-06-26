Title: Pelican 更换主题  
Date: 2016-06-26 10:11  
Category:Pelican  
Tags: python,pelican,markdown


####pelican-themes 命令

pelican-themes是管理主题的命令工具

#####一些基本用法： 


命令

描述

<table>
<tr><td>pelican-themes -h</td><td>显示帮助</td></tr>  
<tr><td>pelican-themes -l</td><td>显示已经安装的主题</td></tr>   
<tr><td>pelican-themes -i [theme_path] </td><td>安装主题</td></tr>   
<tr><td>pelican-themes -r [theme_name] </td><td>删除主题</td></tr>  
</table>

####安装主题

到https://github.com/getpelican/pelican-themes可以下载很多主题

我这里选用Octopress Theme for Pelican 下载zip，然后解压，安装：

`pelican-themes -i /e/pelican/pelican-octopress-theme/`


####应用主题

到你所在站点的目录，有一个pelicanconf.py文件，添加或者修改THEME

`THEME = "pelican-octopress-theme"`


####重新生成html

`pelican content`

####END

