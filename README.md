# OlyLog

> 便捷、灵敏、持续开发。

## 目录

1. 介绍
2. 用法
3. 展望
4. 开原许可

## 介绍

便捷、灵敏、持续开发。

## 用法

### Logger

```python
import olylog
```

在使用`olylog`模块之前需要导入该模块。

```python
logger1=olylog.Logger("logger1")
```

`Logger`是`olylog`里面负责日志记录的类。你需要指定它的名称。

> Tips: 最好起具有代表性的名称，如**函数名**、**类名**等。

下面是`Logger`类里面的函数：

- trace(msg): 记录trace级别的日志。
- debug(msg): 记录debug级别的日志。
- info(msg): 记录info级别的日志。
- warn(msg): 记录warn级别的日志。
- error(msg): 记录error级别的日志。
- fatal(msg): 记录fatal级别的日志。
- stop(): 结束日志记录。

想要个性化？你可以写一个**配置文件**：

```json
{"logger1":{"path":"./olylog/","format":"log","output":"file"}}
```

配置文件的名称必须为`settings.json`。键为Logger对象的名称，值为参数列表。默认`path`为`./log/`，`format`为`log`，`output`为`file`。下面是所有参数：

- path: 日志输出目录，默认为./log/。
- format: 日志输出格式，目前有log和json，默认为log。
- output: 日志输出地点，目前只有file，默认为file。

## 展望

- 配置文件可以设置error和fatal单独输出到errors.log里。
- 一定时间/大小后存储，设置在settings.json里。
- 日志模板自定义。
- 支持用XML输出。
- error预警。
- 日志备份到其他主机。
- 支持集中式。

## 开原许可

遵循AGPL开源协议。
