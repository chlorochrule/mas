# mas v1.0.0 documentation

## mas.MAS
`mas.MAS(cls)`  
**cls** : `Agent`, `AgentGroup`, `Env`クラスのいずれか．  

`Agent`, `AgentGroup`, `Env`クラスのスーパークラス．
このクラスのインスタンスを直接作ることはない．
`Agent`, `AgentGroup`, `Env`クラスそれぞれのインスタンスに固有の識別番号をつける．  
![mas overview](https://raw.githubusercontent.com/chlorochrule/mas/images/mas1.png)  
このように複数の環境やエージェントグループを作っても， それぞれに固有の識別番号が振られる．  

### Attributes  
- **name**  
インスタンスの名前．インスタンス作成時にクラス名と識別番号で初期化される．
変更可能．  

### Methods
- **get_no**(*self*)  
インスタンス固有の識別番号(1~)を返す関数．  

ex.  
```python
agent = Agent()
agent.get_no()  #1
```

## mas.Agent
`mas.Agent(name=None)`  
**name** : エージェント[<sup>\*1</sup>](#annot1)の名前．  

<a id="annot1">\*1</a> `Agent`クラス（またはそのサブクラス）のインスタンス．
以下同様．  

エージェントを表すクラス．
実際に使用するときはこのクラスを継承して必要な機能を追加する．  

ex.  
```python
#mas.Agentを継承して新しいエージェントクラスを作る．
class NeoAgent(mas.Agent):
    #NeoAgent特有の機能や性質を記述する．
```

## mas.AgentGroup
`mas.AgentGroup(agents=None, name=None)`  
**agents** : エージェントグループ[<sup>\*2</sup>](#annot2)
に追加するエージェントまたはエージェントのリスト（タプル）．  
**name** : グループの名前．  

<a id="annot2">\*2</a> `AgentGroup`クラス（またはそのサブクラス）のインスタンス．
以下グループと表記．  

エージェントのグループを表すクラス．
実際に使用するときはこのクラスを継承して必要な機能や性質を追加する．
属するエージェントをイテレート可能．`len()`関数で属するエージェントの数を取得できる．  

ex.  
```python
#mas.AgentGroupを継承して新しいエージェントグループクラスを作る．
class NeoAgentGroup(mas.AgentGroup):
    #NeoAgentGroup特有の機能や性質を記述する．

#10人のグループを作成する．
neo_group = NeoAgentGroup(agents=[Agent() for _ in range(10)])
#10回繰り返す．
for agent in neo_group:
  agent.name  #エージェントの名前の取得．
len(neo_group)  #グループに属するエージェントの総数．
```

### Attributes  
- **agents**  
属するエージェントのリスト．
エージェントの追加や削除は直接行わずに[後述する関数](#add_agent)を使う．  

- **removed_agents**  
`remove_agent()`関数によってグループから削除されたエージェントのリスト．  

### Methods  
- **set_label**(*self, label*)/**get_label**(*self*)  
グループラベルのsetter/getter．グループラベルの詳細は[こちら](#annot4)．  

- <a id="add_agent"></a>**add_agent**(*self, agents*)  
*agents* : エージェントまたはエージェントのリスト（タプル）．  
受け取ったエージェント*agents*をグループに追加する関数．
`mas.AgentGroup.agents`を直接操作せずにこの関数を用いる．  

- **remove_agent**(*self, agents*)  
*agents* : エージェントまたはエージェントのリスト（タプル）．  
受け取ったエージェント*agents*をグループから削除する関数．
`mas.AgentGroup.agents`を直接操作せずにこの関数を用いる．  

- **is_existing_agent**(*self, agent_no*)  
*agent_no* : エージェントの識別番号または識別番号のリスト（タプル）．  
<u>*Return*</u> : bool(`True` or `False`)  
*agent_no*で与えられた識別番号を有するエージェントがグループに属するかを判定し，
属する場合は`True`を返す．識別番号*agent_no*がリスト（タプル）で与えられた場合は，
それぞれの識別番号を有するエージェントがすべてグループに属する場合に`True`を返す．
それ以外は`False`を返す．  

- **get_all_agent_no**(*self, excep=None*)  
*excep* : エージェントまたはエージェントのリスト（タプル）．  
<u>*Return*</u> : エージェントの識別番号のリスト．  
グループに属するエージェントのうち，
*excep*で除外したエージェント以外のすべてのエージェントの識別番号を取得する関数．  

- **get_all_agents**(*self, excep=None*)  
*excep* : エージェントまたはエージェントのリスト（タプル）．  
<u>*Return*</u> : エージェントのリスト．  
グループに属するエージェントのうち，
*excep*で除外したエージェント以外のすべてのエージェントを取得する関数．  

- **get_agents_rand**(*self, num=1, excep=None*)  
*num* : 整数(int)  
*excep* : エージェントまたはエージェントのリスト（タプル）．  
<u>*Return*</u> : エージェントのリスト．  
グループに属するエージェントのうち，
*excep*で除外したエージェント以外のすべてのエージェントの中から，
無作為に*num*個のエージェントを取得する関数．  

## mas.Env
`mas.Env(groups=None, labels=None, name=None)`  
**groups** : 環境[<sup>\*3</sup>](#annot3)
に追加するグループまたはグループのリスト（タプル）．  
**labels** : グループラベル[<sup>\*4</sup>](#annot4)またはラベルのリスト  
**name** : 環境の名前．  

<a id="annot3">\*3</a> `Env`クラス（またはそのサブクラス）のインスタンス．
以下同様．  

<a id="annot4">\*4</a> 環境に属する`AgentGroup`クラス（またはそのサブクラス）
のインスタンスにつけられたエイリアス．例えば環境クラスのインスタンスを`env`,
環境クラスに属するグループ`group1`のグループラベルを`'g1'`とした場合，`env.g1`で
`group1`にアクセスすることができる．グループラベルは文字列(str)で与えられる．
以下ラベルと表記．  

環境を表すクラス．
実際に使用するときはこのクラスを継承して必要な機能や性質を追加する．
属するグループをイテレート可能．`len()`関数で属するグループの数を取得できる．  

ex.  
```python
#mas.Env
class NeoEnv(mas.Env):
    #NeoEnv特有の機能や性質を記述する．

#10人のグループを作成する．
ag1 = AgentGroup(agents=[Agent() for _ in range(10)])
#20人のグループを作成する．
ag2 = AgentGroup(agents=[Agent() for _ in range(20)])
#ag1とag2のグループが属する環境を作成する．
neo_env = NeoEnv(groups=[ag1, ag2], labels=['ag1', 'ag2'])
neo_env.ag1  #neo_envに属するグループag1
#2回繰り返す．
for group in neo_env:
  group.name  #グループの名前の取得．
len(neo_env)  #環境に属するグループの総数．
```

### Attributes  
- **groups**  
属するグループのリスト．
グループの追加や削除は直接行わずに[後述する関数](#add_group)を使う．  

- **removed_groups**  
`remove_group()`関数によって環境から削除されたグループのリスト．  

### Methods  
- **set_label**(*self, group, label*)  
*group* : グループ  
*label* : ラベル(str)  
グループ*group*にラベル*label*を追加する関数．これにより，
*group*オブジェクトに*label*のエイリアスでアクセス可能となる．  

- <a id="add_group"></a>**add_group**(*self, groups*)  
*groups* : グループまたはグループのリスト（タプル）．  
受け取ったグループ*groups*を環境に追加する関数．
`mas.AgentGroup.groups`を直接操作せずにこの関数を用いる．  

- **remove_agent**(*self, groups*)  
*groups* : グループまたはグループのリスト（タプル）．  
受け取ったグループ*groups*を環境から削除する関数．
`mas.AgentGroup.groups`を直接操作せずにこの関数を用いる．  

- **is_existing_group**(*self, group_no*)  
*group_no* : グループの識別番号または識別番号のリスト（タプル）．  
<u>*Return*</u> : bool(`True` or `False`)  
*group_no*で与えられた識別番号を有するグループが環境に属するかを判定し，
属する場合は`True`を返す．識別番号*group_no*がリスト（タプル）で与えられた場合は，
それぞれの識別番号を有するグループがすべて環境に属する場合に`True`を返す．
それ以外は`False`を返す．  

- **get_all_group_no**(*self, excep=None*)  
*excep* : グループまたはグループのリスト（タプル）．  
<u>*Return*</u> : グループの識別番号のリスト．  
環境に属するグループのうち，
*excep*で除外したグループ以外のすべてのグループの識別番号を取得する関数．  

- **get_all_groups**(*self, excep=None*)  
*excep* : グループまたはグループのリスト（タプル）．  
<u>*Return*</u> : グループのリスト．  
環境に属するグループのうち，
*excep*で除外したグループ以外のすべてのグループを取得する関数．

- **get_all_agents**(*self, excep=None*)  
*excep* : エージェントまたはエージェントのリスト（タプル）．  
<u>*Return*</u> : エージェントのリスト．  
環境に属するエージェントのうち，
*excep*で除外したエージェント以外のすべてのエージェントを取得する関数．  

- **get_agents_rand**(*self, num=1, excep=None*)  
*num* : 整数(int)  
*excep* : エージェントまたはエージェントのリスト（タプル）．  
<u>*Return*</u> : エージェントのリスト．  
環境に属するエージェントのうち，
*excep*で除外したエージェント以外のすべてのエージェントの中から，
無作為に*num*個のエージェントを取得する関数．  

## mas.MasException  
`mas.MasException(e)`  
**e** : エラーメッセージ(str)  

マルチエージェントシステムの仕様に関するエラーのための例外クラス．
実際に使うときにはこのクラスを継承して新しい例外クラスを作り，
そこに処理を記述する．  
