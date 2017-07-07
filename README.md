#   pathon 爬虫

##  安装python环境（version 3以下操作）

### 安装pyenv (Python 多版本管理器)
自动安装工具
$ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
在上述运行完之后通常在命令行中会提示：
WARNING: seems you still have not added 'pyenv' to the load path.
<pre>执行：
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    $ source ~/.bashrc
或者：
    printf'export PATH="$HOME/.pyenv/bin:$PATH"\neval "$(pyenv init -)"\neval "$(pyenv virtualenv-init -)"\n'>>~/.bashrc
使之生效，这样我们的pyenv算是初步安装成功了;
</pre>
####  安装最新python3
<pre>
下载包文件：
$ wget wget  https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tar.xz （yum search xz 解包依赖）；
</pre>           
##### 编译
<pre>
tar Jxvf  Python-3.5.0.tar.xz
cd Python-3.5.0
./configure --prefix=/usr/local/python3
make && make install
</pre>
####  设置环境变量
<pre>
echo 'export PATH=$PATH:/usr/local/python3/bin' >> ~/.bashrc
或者可以直接替换python2
rm   /usr/bin/pythonln -sv  /usr/local/bin/python3.5 /usr/bin/python

这样做的目的是在系统任意目录敲入python调用的是python3的命令，而非系统默认2.6.6的
但是这样同时这会导致依赖python2.6的yum不能使用，因此还要修改yum配置。
</pre>
####  更新yum配置。
<pre>
ll /usr/bin | greppython
这时/usr/bin目录下面是包含以下几个文件的（ll |greppython），其中有个python2.6，只需要指定yum配置的python指向这里即可
vim /usr/bin/yum
通过vim修改yum的配置
#!/usr/bin/python改为#!/usr/bin/python2.6，保存退出。
完成了python3的安装。
</pre>
####  先下载get-pip.py,
* wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
* python get-pip.py 
##  搭建scrapy
<pre>
教程地址：
http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/install.html
</pre>
安装依赖 
* pip install  PIL
* pip install pymongo3
* pip install pillow


