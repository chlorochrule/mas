# Python Tutorial for mas  
mas.pyを使う上で知っておいたほうがいいPythonやオブジェクト指向の知識を簡単にまとめておきます．  

## オブジェクト指向(Object-oriented)  
オブジェクト指向プログラミングでは，データと処理の集まりを一つのオブジェクトとして表現する．  

### クラスとインスタンス(Class and Instance)  
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

### 属性とメソッド(Attribute and Method)  
オブジェクトは属性とメソッドを持つ．  

- **属性**(Attribute)  
オブジェクトの持つ変数みたいなもの．  

- **メソッド**(Method)  
オブジェクトの持つ関数みたいなもの．
Pythonではインスタンスが生成されたときに`__init__`メソッドが呼ばれる．  

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
#このとき __init__ メソッドの an_type につぶあんが渡される．
taiyaki = TaiyakiClass('tsubuan')  #インスタンス生成
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
ここで，`self`にはインスタンス自身`taiyaki`が，`an_type`には`koshian`が渡される．  

インスタンス`ins`の属性`ins_attr`にアクセスするときは`ins.ins_attr`のようにする．  
インスタンス`ins`のメソッド`ins_method`にアクセスするときは`ins.ins_method()`のようにする．  

### クラス属性とクラスメソッド(Class method and Class attribute)
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

### 継承(Inheritance)  
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

### カプセル化(Encapsulation)  
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

### Digression
Pythonのオブジェクトに関する余談を少々．
実用性のない話が多いので読み飛ばしてもらってかまいません．  

#### type
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

#### object
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

#### 抽象クラス/インターフェース
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

#### 多重継承
Pythonは数少ない多重継承をサポートしている言語である．  

```python
class MultiInheritClass(Base1, Base2, Base3):
```

探索は左から順に解決され，`super()`で呼んだ場合，一番左のクラス`Base1`が呼ばれる．
使いどころはいまいち分からない．  

#### 新スタイルクラス/旧スタイルクラス
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

#### \_\_new\_\_(cls, \*args)
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

#### オーバーロード
Pythonはインタプリタ言語のため，オーバーロードには対応していない．
型による分岐を行うときは`isinstance`メソッドを使う．  

```python
if isinstance(x, (int, long)):
  #整数型の場合の処理．longを書くのは2のみ．
if isinstance(x, float):
  #実数型の場合の処理．
```

#### 関数
関数，メソッドはオブジェクトでない．

```python
def func1():
  pass

func2 = lambda x: x

type(func1)  #<type 'function'>
type(func2)  #<type 'function'>
type(sum)  #<type 'builtin_function_or_method'>
type(str.replace)  #<type 'method_discriptor'>

type(function)  #NameError: name 'function' is not defined
type(builtin_function_or_method)  #NameError: name 'builtin_function_or_method' is not defined
type(method_discriptor)  #NameError: name 'method_discriptor' is not defined
```

このように関数やメソッドを`type`で判別してもエラーにはならないが，オブジェクトではない．  

#### 隠し属性
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
