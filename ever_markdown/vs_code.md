---
title: vs code、anaconda各种DL环境配置安装-markdown
tags: vs code
notebook: tools
---

## tensorflow相关

### 在vs code安装python插件步骤

1. 打开VScode，shift + cmd +p 
2. 输入 “ext install python”，搜索时间可能会比较长 
3. 选择下载量最高的那个python插件点击安装（直接等待安装好就好了） 

这里就可以写python程序了，默认按F5后需要再按一次F5程序就可以运行程序了，如果要按F5马上运行需要将launch.json文件的 “stopOnEntry”: true,改为 “stopOnEntry”: false。

### 在anaconda和vs安装tensorflow
1. 直接在anaconda "Environments"里搜TensorFlow，安装就行
2. 注意要在vs code用TensorFlow的话，需要配置：
"python.pythonPath":"/anaconda3/envs/tensorflow/bin/python3.6",
"python.autoComplete.extraPaths": [
"/anaconda3/envs/tensorflow/lib/python3.6/site-packages"
],
要填写用anaconda里装了TensorFlow环境的python目录

### 配置yapf
> 安装yapf之后在VScode中按Alt+Shift+F即可自动格式化代码 
1. 打开终端命令行
2. 输入 “pip install yapf” 或者 “conda install yapf”
3. 安装yapf成功后，打开VScode，文件->首选项->用户设置，在settings.json文件中输入”python.formatting.provider”: “yapf”

### 配置flake8
> 安装flake8之后写代码的时候编辑器就会提示哪里出错，代码格式不规范也会提示 
1. 打开命令行
2. 输入“pip/conda install flake8”
3. 安装flake8成功后，打开VScode，文件->首选项->用户设置，在settings.json文件中输”python.linting.flake8Enabled”: true

---
## evermonkey/evernote/markdown相关

### 为避免markdown文件中控制字符造成ever publish失败要配置
"editor.renderControlCharacters": true,
控制编辑器是否应呈现控制字符，这样控制字符能够显示出来，文件里没有控制字符才能成功同步到evernote
