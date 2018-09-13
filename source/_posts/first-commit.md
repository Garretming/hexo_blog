---
title: first commit blog
---
今天刚搭好hexo,尝试一下提交文章到博客；


## 步骤：

### 1、编辑Markdown
由于知道怎编辑，所以就直接用编辑器编辑；不知道的话可以以使用CSDN网上面提供的MarkDown编辑器 http://write.blog.csdn.net/mdeditor (在csdn博客写新文章的时候能切换到这种编辑器)，写好文章后，找到菜单栏的“导出到本地”选项  菜单 
以md格式导出到本地，然后copy该md文件，粘贴到你当初建的博客站点文件夹下的source\ _posts目录下，一个md文件对应一篇博客文章。

### 2、清理静态页面

``` bash
$ hexo clean
```
或者直接 省略下面的几步：       
``` bash
$ hexo clean
$ hexo d -g
```

### 3、生成静态页面

输入：hexo generate，回车，生成静态页面。
``` bash
$ hexo g
```

### 4、预览

再输入：hexo server，回车，到localhost:4000预览博客效果， 

``` bash
$ hexo s
```

### 5、同步

最后输入：hexo deploy，回车，同步到github上去就行了。
``` bash
$ hexo d
```

