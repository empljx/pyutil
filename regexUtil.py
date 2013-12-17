# -*- coding: utf-8 -*-

import  re

'''
1. 字符
. 匹配一般字符
\ 转义
[...] 字符集。[abc], [a-z]。如果以 ^ 开头，表示取反: [^abc] 不是以abc开头。

2. 预定义字符集
\d 数字 = [0-9]
\D 非数字 = [^0-9]
\s 空白字符 = [<空格>\t\r\n\f\v]
\S 非空白字符 = [^\s]
\w 单词字符 = [A-Za-z0-9_]
\W 非单词字符 = [^\w]

3. 数量词
        匹配前一个字符
*     0次或多次
+     一次或多次
?     0次或多次
{m}    m次
{m,n}  m到n次。{,n}={0,n}, {m,}=m到无限次

4. 边界匹配
^ 匹配字符串开头，是多个字符，在多行模式中匹配每一行开头。
$ 匹配字符串结尾......
\A 仅匹配字符串开头
\Z 仅匹配字符串结尾
\b 匹配 \w 和 \W 之间
\B [^\b]

5. 逻辑 分组
| 左右表达式中任意匹配一个，先匹配左边，如果成功直接完成。 = or
(...) 进行分组，括号括起来为一个整体
(?P<name>...) 分组，给该组起个别名
\<number> 引用编号为<number>的分组匹配到的字符串 (\d)abc\1 = 1abc1
(?P=name) 引用别名为<name>的匹配到的字符串 (?P<id>\d)abc(?P=id) = 1abc1
?iLmsux : iLmsux 是匹配模式

\　转义， r"\\d"
'''

'''
compile 的第二个参数 flag:
比如re.compile('pattern', re.I | re.M)与re.compile('(?im)pattern')是等价的。
选值有：
    re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
   re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
    re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
    re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
    re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
    re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

pattern 只能通过re.compile() 得到
pattern 对象的属性：

pattern 对象的属性：
'''




'''
match 对象属性
string: 匹配时使用的文本。
re: 匹配时使用的Pattern对象。
pos: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
endpos: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
lastindex: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。

match 对象方法

group([group1, …])：
获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；
没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
groups([default])： 
以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
groupdict([default])：
返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
start([group])： 
返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
end([group])：
返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
span([group])：
返回(start(group), end(group))。
expand(template)： 
将匹配到的分组代入template中然后返回。template中可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。
\id与\g<id>是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符'0'，只能使用\g<1>0。
'''
def matchUtil():
    regex = r"(\w+) (\w+)(?P<sign>.*)"
    pattern = re.compile(regex, re.I)
    
    source = "hello world!!"
    match = pattern.match(source)
    
    print match.string
    print match.re
    print match.pos
    print match.endpos
    print match.lastindex
    print match.lastgroup
    
    print 
    print match.group()
    print match.group(1, 2)
    print match.groups()
    print match.groupdict()
    print match.start(2)
    print match.end(2)
    print match.span(2)
    print match.expand(r"\2 \1\3")


