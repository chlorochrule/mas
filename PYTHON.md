# Python Tutorial for mas  
mas.pyを使う上で知っておいたほうがいい[オブジェクト指向](#OOP)や[Python](#Python)の知識を簡単にまとめておきます．  

## 目次
- [オブジェクト指向](#OOP)
 - [クラスとインスタンス](#classinstance)
 - [属性とメソッド](#attrmethod)
 - [クラス属性とクラスメソッド](#clsattrmethod)
 - [継承](#inheritance)
 - [カプセル化](#encap)
 - [Digression](#digression)
   - [type](#type)
   - [object](#obj)
   - [抽象クラス/インターフェース](#abc)
   - [多重継承](#minheritance)
   - [新スタイルクラス/旧スタイルクラス](#newclsoldcls)
   - [\_\_new\_\_(cls, \*args)](#new)
   - [オーバーロード](#overload)
   - [関数](#func1)
   - [隠し属性](#encapattr)
- [Python for mas.py](#Python)
 - [リスト/タプル](#listtuple)
 - [リスト内包表記](#listin)
 - [関数](#func2)
 - [Mutable/Immutable](#mutable)
 - [Copy/Deepcopy](#copydeepcopy)
- [mas.py注意点](#annotmas)
 - [エージェントの生成](#genagents)

## <a id="OOP"></a>オブジェクト指向(Object-oriented)
オブジェクト指向プログラミングでは，データと処理の集まりを一つのオブジェクトとして表現する．  

### <a id="classinstance"></a>クラスとインスタンス(Class and Instance)  
オブジェクトにはクラスとインスタンスがある．  

- **クラス**(Class)  
オブジェクトの設計図．たいやきの鋳型みたいなイメージ．  

- **インスタンス**(Instance)  
設計図（クラス）から作られた実体．たいやきみたいなイメージ．  

![taiyaki](http://image.itmedia.co.jp/im/articles/0506/11/object10_01.gif)  

こんなイメージ．  

#### Python  
Pythonで書くとこんな感じ．  
ex.  
```python
class TaiyakiClass:  #クラス定義
  pass    #何もしない

taiyaki = TaiyakiClass()    #インスタンス生成
```  

`class TaiyakiClass:` ... TaiyakiClassクラスの宣言．  
`TaiyakiClass()` ... TaiyakiClassクラスのインスタンスの生成．  

### <a id="attrmethod"></a>属性とメソッド(Attribute and Method)  
オブジェクトは属性とメソッドを持つ．  

- **属性**(Attribute)  
オブジェクトの持つ変数みたいなもの．  

- **メソッド**(Method)  
オブジェクトの持つ関数みたいなもの．
Pythonではインスタンスが生成されたときに`__init__()`メソッドが呼ばれる．  

#### Python  
Pythonで書くとこんな感じ．  
ex.  
```python
class TaiyakiClass:
  def __init__(self, an_type):  #初期化メソッド
    self.an = an_type

  def set_an(self, an_type):  #あんをセットするメソッド
    self.an = an_type
#インスタンス生成．
#このとき __init__ メソッドの an_type に'tsubuan'が渡される．
taiyaki = TaiyakiClass('tsubuan')
taiyaki.an  #'tsubuan'
taiyaki.set_an('koshian')
taiyaki.an  #'koshian'
```

`TaiyakiClass('tsubuan')` ...TaiyakiClassクラスのインスタンスの生成．引数`'tsubuan'`は，
`__init__()`メソッドの**第2引数**(an_type)に渡される．  

`def __init__(self, an_type):` ...インスタンスが生成されたときに呼び出される初期化メソッド．
`self`には作成されたインスタンスが，
`an_type`にはインスタンス作成時に指定された引数`'tsubuan'`が渡される．  

`def set_an(self, an_type):` ...通常のメソッド．インスタンスを`taiyaki`とすると，
`taiyaki.set_an('koshian')`のように呼ばれる．
ここで，`self`にはインスタンス自身である`taiyaki`が，`an_type`には`koshian`が渡される．  

インスタンス`ins`の属性`ins_attr`にアクセスするときは`ins.ins_attr`のようにする．  
インスタンス`ins`のメソッド`ins_method`にアクセスするときは`ins.ins_method()`のようにする．  

### <a id="clsattrmethod"></a>クラス属性とクラスメソッド(Class method and Class attribute)
インスタンスに対する操作はたいやきに対する操作を想像してもらえればよい．
例えば，たいやき`taiyaki`にあん`'koshian'`を入れる操作は`taiyaki.set_an('koshian')`と記述できた．
これに対し，クラスメソッドはたいやきの鋳型に対する操作である（例えば，たいやきに刻印する模様を変更するなど）．
クラスメソッドはインスタンスからではなく，クラス自身から直接呼び出す．  

#### Python
Pythonで書くとこんな感じ．  
ex.  
```python
class TaiyakiClass:
  mark = 'tai'  #クラス属性（クラス変数）
  #中略
  @classmethod  #クラスメソッドのデコレータ
  def change_mark(cls, new_mark):  #クラスメソッド change_mark
    cls.mark = new_mark  #クラス属性 cls.mark を new_mark に変える．

TaiyakiClass.mark  #'tai'
#TaiyakiClassクラスのクラス属性 mark を'tai'から'fugu'に変える．
TaiyakiClass.change_mark('fugu')  
TaiyakiClass.mark  #'fugu'
```

`TaiyakiClass.mark` ...`TaiyakiClass`クラスのクラス属性`mark`．  

`def change_mark(cls, new_mark):` ...`TaiyakiClass`クラスのクラスメソッド．
`TaiyakiClass.change_mark('fugu')`のように呼ばれる．
ここで，`cls`には`TaiyakiClass`クラス自身が，`new_mark`には`'fugu'`が渡される．  

クラス属性，クラスメソッドではクラス自身から呼び出し，クラス自身に対して操作を行う．  

`@classmethod`については [Python デコレータ](https://www.google.co.jp/search?q=python%20%E3%83%87%E3%82%B3%E3%83%AC%E3%83%BC%E3%82%BF) で検索！

### <a id="inheritance"></a>継承(Inheritance)  
クラス`A`がクラス`B`を継承した場合．クラス`A`はクラス`B`の属性，メソッドを引き継ぎ，
さらにクラス`A`特有の属性やメソッドを追加で定義できる．
このとき継承してできた新しいクラスを子クラス（サブクラス）といい，
継承されたクラスを親クラス（スーパークラス）という．  

#### Python  
Pythonで書くとこんな感じ．  
```python
#親クラス
class TaiyakiClass:
  def __init__(self, an_type):
    self.an = an_type

  def set_an(self, an_type):
    self.an = an_type

#子クラス
#TaiyakiClassを継承して，新しくShiroiTaiyakiClassを定義する．
class ShiroiTaiyakiClass(TaiyakiClass):
  def __init__(self, an_type, color):
    #親クラス(TaiyakiClass)の初期化メソッド __init__ の呼び出し．
    super().__init__(an_type)  
    self.color = 'white'  #新しい属性

  def set_color(self, color):  #新しいメソッド
    self.color = 'white'

shiroitaiyaki = ShiroiTaiyakiClass('tsubuan', 'white')
shiroitaiyaki.an  #'tsubuan'
shiroitaiyaki.set_an('koshian')
shiroitaiyaki.color  #'white'
```

`class ShiroiTaiyakiClass(TaiyakiClass):` ...このようにクラス名の後のカッコの中に親クラスを指定することで継承することができる．
子クラス`ShiroiTaiyakiClass`は親クラス`TaiyakiClass`の属性とメソッドを有する．  

子クラスでは親クラスで既に定義されているメソッドを再定義することができる（オーバーライド）  

### <a id="encap"></a>カプセル化(Encapsulation)  
オブジェクト内部の処理やデータを隠ぺいしようとする考え方．
外部からオブジェクトの属性やメソッドを利用しないことを保障することで，
仕様の変更が与える影響の範囲を限定する．  

#### Python  
Pythonではオブジェクトの外部からのアクセスを完全に禁止する方法がない．
しかし，外部からのアクセスを推奨しない属性，メソッドには名前の前に`_`（アンダースコア）をつける慣習がある．
より強固なアクセス制限をしたい場合には，名前の前に`__`（アンダースコア2つ）をつける．
この場合，属性またはメソッドに直接はアクセスできなくなる．  

```python
class ProtectedClass:
  def __init__(self):
    self._attr1 = 'attr1'
    self.__attr2 = 'attr2'

pc = ProtectedClass()
pc._attr1  #'attr1'
pc.__attr2  #AttributeError: 'ProtectedClass' object has no attribute '__attr2'
pc._ProtectedClass__attr2  #'attr2'
```

このように，アンダースコア1つだと一応通常通りアクセス可能だが，
アンダースコアを2つ付けた場合には`_ProtectedClass__attr2`としないとアクセスできない．

### <a id="digression"></a>Digression
Pythonのオブジェクトに関する余談を少々．
実用性のない話が多いので読み飛ばしてもらってかまいません．
興味がなければ[こちら](#Python)．  

#### <a id="type"></a>type
Pythonのすべてのクラスは`type`クラスのインスタンスとなっている．
組み込み関数`type`はオブジェクトの型（そのインスタンスを生成したクラス）を返す．  

```python
type(1)  #<type 'int'>
type('abc')  #<type 'str'>
type(int)  #<type 'type'>
type(object)  #<type 'type'>
type(type)  #<type 'type'>
```

ここで面白いのが`type`クラスも`type`クラスのインスタンスとなっているところ．
自分自身を生成するような鋳型というものが現実にはないのでなかなかイメージしにくい．  

#### <a id="obj"></a>object
Pythonの`object`クラス以外のすべてのクラスは`object`クラスを最上位のクラスとして継承している．  

```python
str.__bases__  #(<type 'basestring'>,)
unicode.__bases__  #(<type 'basestring'>,)
basestring.__bases__  #(<type 'object'>,)
int.__bases__  #(<type 'object'>,)
long.__bases__  #(<type 'object'>,)
type.__bases__  #(<type 'object'>,)
object.__bases__  #()
```

`object`クラス以外のすべてのクラスは上位クラスとしてオブジェクトを継承しているのが分かる．
`object`クラスは継承しているクラスがないので`__bases__`に`()`が格納されている．
Python2において`str`クラスと`unicode`クラスは`basestring`クラスを基底クラスとして持つが，
`int`クラスと`long`クラスには共通の基底クラスがない．
にもかかわらず整数の大きさに応じて暗黙的な型変換が起こるためエラーを招きやすい．
Python3では整数型は`int`に統一されている．Python3を使おう．  

#### <a id="abc"></a>抽象クラス/インターフェース
Pythonでは下位クラスに実装を強制するような仕組みがない．
しかし，`abc`モジュールを使うことで疑似的に抽象クラスを実装できる．  

```python
from abc import ABCMeta

class ABClass:
    __metaclass__ = ABCMeta   #class ABClass(metaclass=ABCMeta):   at Python3

    @abstractmethod
    def must_implements(self):
        pass
```

#### <a id="minheritance"></a>多重継承
Pythonは数少ない多重継承をサポートしている言語である．  

```python
class MultiInheritClass(Base1, Base2, Base3):
```

探索は左から順に解決され，`super()`で呼んだ場合，一番左のクラス`Base1`が呼ばれる．
使いどころはいまいち分からない．  

#### <a id="newclsoldcls"></a>新スタイルクラス/旧スタイルクラス
Python2には旧スタイルクラスと新スタイルクラスがある．  

```python
class OldStyleClass:  #旧スタイルクラス
  pass

class NewStyleClass(object):  #新スタイルクラス
  pass

type(OldStyleClass)  #<type 'classobj'>
type(NewStyleClass)  #<type 'object'>
```

Python3からは新スタイルクラスのみとなった．
Python2でも旧スタイルクラスを使うメリットはないので新スタイルクラスを使おう．  

#### <a id="new"></a>\_\_new\_\_(cls, \*args)
Pythonにはインスタンスの初期化メソッドとして`__init__()`があるが，
それとは別に`__new__()`メソッドがある．
`__init__()`はインスタンスを受け取り初期化するインスタンスメソッドだが，
`__new__()`はクラスを受け取りインスタンスを作成して返却する，クラスメソッドである．
インスタンスの初期化処理は通常`__init__()`に記述する．  

```python
class MyClass:
  def __new__(cls, *args):
    #Return instance of cls

  def __init__(self, *args):
    #Initialize instance self
```

`__new__`，`__init__`の順で呼び出されるが，`__new__`メソッドをオーバーライドする機会はあまりない．  

#### <a id="overload"></a>オーバーロード
Pythonはインタプリタ言語のため，オーバーロードには対応していない．
型による分岐を行うときは`isinstance`メソッドを使う．  

```python
if isinstance(x, (int, long)):
  #整数型の場合の処理．longを書くのは2のみ．
if isinstance(x, float):
  #実数型の場合の処理．
```

#### <a id="func1"></a>関数
関数，メソッドはオブジェクトでない．

```python
def myfunc1():
  pass

myfunc2 = lambda x: x

type(myfunc1)  #<type 'function'>
type(myfunc2)  #<type 'function'>
type(sum)  #<type 'builtin_function_or_method'>
type(str.replace)  #<type 'method_discriptor'>

type(function)  #NameError: name 'function' is not defined
type(builtin_function_or_method)  #NameError: name 'builtin_function_or_method' is not defined
type(method_discriptor)  #NameError: name 'method_discriptor' is not defined
```

このように関数やメソッドを`type`で判別してもエラーにはならないが，オブジェクトではない．  

#### <a id="encapattr"></a>隠し属性
クラスには隠し属性が存在する．隠し属性は`__class__`のようにアンダースコア2つで囲われている．  

```python
class MyClass:
  pass

mc = MyClass()

mc.__class__  #クラス定義．この場合は MyClass.
mc.__dict__  #全属性をディクショナリ化したもの．
mc.__str__()  #クラスを文字列化するためのメソッド．

```

他にもいろいろある．

## <a id="Python"></a>Python for mas.py
ここからはPythonについて説明していきます．
分からない用語やシンタックスがあれば[こちら](http://www.python-izm.com/)を参照．  

### <a id="listtuple"></a>リスト/タプル(list/tuple)
PythonにはC言語の配列の代わりにリストとタプルがある．  

- リスト(`list`)  
可変長の配列であり，要素の追加，削除，変更が可能．  

- タプル(`tuple`)  
固定長の配列であり，要素の追加，削除，変更が不可能．  

```python
mylist = range(10)  #[0, 1, 2, ..., 9]
mytuple = tuple(range(10))  #(0, 1, 2, ..., 9)
##要素の取得．リスト，タプル共通
print mylist[0]
#>>>0
print mylist[-1]
#>>>9
print mylist[1:3]
#>>>[1, 2]

##要素の操作
mylist[0] = 10
#mylist: [10, 1, 2, ..., 9]
mytuple[0] = 10
#TypeError: 'tuple' object does not support item assignment
```

このように`:`で区切ることにより，部分リストや部分タプルを取得することができる．
例えば`mylist`の最後の要素以外のリストを取得したい場合などは，
`mylist[:-1]`と書くことができる．
このようにして得られた部分リストをPythonでは**スライス**という．  

<!-- 文字列の内容は今回のmas.pyを使う上であまり重要でないと判断しました．-->
<!--
### 文字列(str)
Python2では文字列に`unicode`型と`str`型があるが，Python3では`unicode`型に統一されている．
Python3の`str`型がPython2の`unicode`型と等価であると思っていただければよい．
Python2では文字列の前にuをつけることで`unicode`文字列として扱う（例：`u'a'`）．
Python2では`str`型と`unicode`型は共通の基底クラスとして`basestring`を持つ．
Python3では文字列の前にbをつけることで`bytes`型として扱うことができる（例：`b'a'`）．
文字列の前にrをつけることで文字列内のエスケープシーケンスを無効化できる．
スライスを用いることで部分文字列を取得することができる．  

```python
##Python2
type(u'a')  #<type 'unicode'>
type('a')  #<type 'str'>

##Python3
type('a')  #<type 'str'>
type(b'a')  #<type 'bytes'>

##Raw string
print 'dir\normal_file'
#>>>dir
#>>>ormal_file
print r'dir\normal_file'
#>>>dir\normal_file

##Slice
mystr = 'abcde'
print mystr[0]
#>>>'a'
print mystr[1:3]
#>>>'bc'
```
-->
### <a id="listin"></a>リスト内包表記
**リスト内のすべての要素に何かしらの処理をしたい**
といった場合に便利なのがリスト内包表記である．

```python
mylist = range(10)  #[0, 1, 2, ..., 9]

##mylist内の要素をすべて二乗したリスト．
print [i**2 for i in mylist]
#>>>[0, 1, 4, ..., 81]
#この処理はmap()関数を使って次のようにも書ける．
print list(map(lambda x: x**2, mylist))
#>>>[0, 1, 4, ..., 81]

##mylist内の要素のうち偶数の要素のみを取り出したリスト．
print [i for i in mylist if i%2 == 0]
#>>>[0, 2, 4, ..., 8]
#この処理はfilter()関数を使って次のようにも書ける．
print list(filter(lambda x: x%2==0, mylist))
#>>>[0, 2, 4, ..., 8]
```

Rubyでは`.each do`や`map`，`select`を多用するが，Pythonでは`for`を多用する．
個人的には`map`と`filter`を一行で実装できるため，リスト内包表記を推奨する．
リスト内包のほかに，ディクショナリ内包やセット内包もある．  

### <a id="func2"></a>関数
Pythonでは関数の引数にデフォルト値をセットすることができるが，デフォルト値は[immutable](#mutable)なオブジェクトでなければならない．
これはデフォルト値の評価が一度しか行われないためである．
リスト，タプルは前方に`*`をつけることで要素を引数として関数に渡すことができる．
リストやタプルを要素に分解することをアンパックという．
ディクショナリのアンパックには`**`を用いる．
関数の引数は可変長の値をとることができる．
この時，関数側では`*`のついた引数がタプルにパックされる．  

```python
def to_tuple(x, y=1):
  return (x, y)

##関数の挙動
print to_tuple(1, 2)
#>>>(1, 2)
print to_tuple(x=1, y=2)
#>>>(1, 2)
print to_tuple(y=1, x=2)
#>>>(2, 1)
print to_tuple(0)
#>>>(0, 1)

##リストのアンパック
args = [1, 2]
print to_tuple(*args)
#>>>(1, 2)

##ディクショナリのアンパック
args = {'x': 1, 'y': 2}
print to_tuple(**args)
#>>>(1, 2)

##可変長引数
def to_tuple(x, y=1, *z):
  return (x, y, z)

print to_tuple(1, 2, 3, 4, 5)
#>>>(1, 2, (3, 4, 5))

##デフォルト引数がmutableなオブジェクトをとった場合
def myappend_1(li=[]):
  li.append(1)
  return li

print myappend_1()
#>>>[1]
print myappend_1()
#>>>[1, 1]
print myappend_1()
#>>>[1, 1, 1]
```

デフォルト引数が[mutable](#mutable)なオブジェクトの場合は上記のような挙動になる．
これは意図しない挙動であると思う．呼び出しごとに`li`を`[]`で初期化したい場合は以下のように書く．  

```python
def myappend_1(li=None):
  li = li if li is not None else []
  return li

  print myappend_1()
  #>>>[1]
  print myappend_1()
  #>>>[1]
  print myappend_1()
  #>>>[1]
```

### <a id='mutable'></a>Mutable/Immutable
mutableなオブジェクトとは作成後に状態を変更可能なオブジェクトである．immutableはその対義語で，作成後に状態を変更不能なオブジェクトである．  

- mutableなオブジェクト  
リスト，ディクショナリ，NumPyの配列(numpy.ndarray)  

- immutableなオブジェクト  
文字列(str)，整数型(int)，タプル  

自作したクラスのインスタンスは属性を操作できるため，（通常は）mutableなオブジェクトである．  

```python
mylist = range(10)
print mylist
#>>>[0, 1, 2, ..., 9]
yourlist = mylist
yourlist[0] = 10
print mylist
#>>>[10, 1, 2, ..., 9]
```

mutableなオブジェクトを別の変数に代入する場合，代入された変数への操作が，代入した変数へ影響を与えることに注意しなければならない．この問題の解決方法は次節で述べる．  

### <a id="copydeepcopy"></a>Copy/Deepcopy
前節で述べた通り，Pythonではmutableなオブジェクトは参照渡しとなる．
もしmutableなオブジェクトを複製したい場合は`copy`モジュールを使う．  

```python
import copy

##代入
mylist = range(10)
yourlist = mylist
print mylist is yourlist
#>>>True

##Copy
mylist = range(10)
print mylist
#>>>[0, 1, 2, ..., 9]
yourlist = copy.copy(mylist)
print mylist is yourlist
#>>>False
yourlist[0] = 10
print yourlist
#[10, 1, 2, ..., 9]
print mylist
#[0, 1, 2, ..., 9]
```

Pythonは`==`で値が等価であるかどうかを判定するが，`is`ではオブジェクトが同一であるかを比較する．例えば，`1==1.0`は`True`となるが，`1 is 1.0`は`False`となる．  

`copy`メソッドを用いることでmutableなオブジェクトを複製することができた．しかし`copy`メソッドでは，mutableなオブジェクトの中にmutableなオブジェクトが入れ子になっている場合，入れ子になっているオブジェクトを複製することができない．このような場合は`deepcopy`メソッドを用いる．  

```python
import copy

##Copy
mylist2 = [range(2) for _ in range(2)]
print mylist2
#>>>[[0, 1], [0, 1]]
yourlist2 = copy.copy(mylist2)
yourlist2[0][0] = 10
print yourlist2
#>>>[[10, 1], [0, 1]]
print mylist2
#>>>[[10, 1], [0, 1]]
print mylist2 is yourlist2
#>>>False
print mylist2[0] is yourlist2[0]
#>>>True

##Deepcopy
mylist2 = [range(2) for _ in range(2)]
print mylist2
#>>>[[0, 1], [0, 1]]
yourlist2 = copy.deepcopy(mylist2)
yourlist2[0][0] = 10
print yourlist2
#>>>[[10, 1], [0, 1]]
print mylist2
#>>>[[0, 1], [0, 1]]
print mylist2 is yourlist2
#>>>False
print mylist2[0] is yourlist2[0]
#>>>False
```

## <a id="annotmas"></a>mas.py注意点
mas.pyを使う上での注意点を書いておきます．  

### <a id="genagents"></a>エージェントの生成
複数のエージェントを生成してリストに格納する場合の注意点．  

```python
##100体のエージェントのグループを作成する場合．
number_of_agents = 100
agents = [Agent() for _ in range(number_of_agents)]
group = AgentGroup(agents=agents)

##ダメな例1
agents = [Agent()] * number_of_agents
#これだと100体のエージェントがすべて同じオブジェクトとなってしまう．

##ダメな例2
agents = [Agent() for _ in range(number_of_agents)]
group1 = AgentGroup(agents=agents)
group2 = AgentGroup(agents=agents)
#これだとグループ1のエージェントとグループ2のエージェントが同一のオブジェクトとなってしまう．
```

例2の場合は`copy`モジュールの`deepcopy`メソッドを用いることで違うオブジェクトとみなすことができるが，エージェントにつけられた通し番号が被ってしまうので好ましくない．
グループに渡すエージェントのリストは以下のようにその都度作成しよう．  

```python
agents1 = [Agent() for _ in range(number_of_agents1)]
group1 = AgentGroup(agents=agents1)
agents2 = [Agent() for _ in range(number_of_agents2)]
group2 = AgentGroup(agents=agents2)
```

*2016/12/21 edited by minami*
