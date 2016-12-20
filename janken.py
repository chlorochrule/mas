#-*- coding: utf-8 -*-
import mas
import time
import random

#じゃんけんのプレイヤーエージェントクラス．
class Player(mas.Agent):
    """docstring for Player."""
    def __init__(self, prob, score=0, name=None):
        super(Player, self).__init__(name=name)
        #プレイヤーの出すハンドの確率分布のリスト． [グーの確率，チョキの確率，パーの確率]
        self.prob = prob
        #じゃんけんの戦績．勝つと+1されて負けると-1される．引き分けはそのまま．
        self.score = score

#強化学習機能を備えたプレイヤーのクラス．Playerクラスのサブクラス．
class ReinPlayer(Player):
    """docstring for ReinPlayer."""
    def __init__(self, prob, score, name=None, alpha=0.05):
        super(ReinPlayer, self).__init__(prob, score, name=None)
        #強化学習の平滑化係数．
        self.alpha = alpha

    def rein_learn(self, hand, res):
        #hand: {0: グー, 1: チョキ, 2: パー}
        #res: {0: 負け, 1: 勝ち, 2: 引き分け}

        #引き分けの場合の処理．何もせずに終了．
        if res == 2:
            return
        #プレイヤーの出したハンドの学習後の確率．
        new_prob = self.alpha*res + (1-self.alpha)*self.prob[hand]
        #学習後の確率と学習前の確率との差．
        diff_prob = new_prob - self.prob[hand]
        #今回プレイヤーが出していないハンドの集合．
        #例えば hand=0 なら others_no = set([1, 2])
        others_no = (set(range(3)) - set([hand]))
        for i in others_no:
            #プレイヤーが出していないハンドの確率を更新（学習）．
            self.prob[i] -= diff_prob / len(others_no)
        #プレイヤーが出したハンドの確率を更新（学習）．
        self.prob[hand] = new_prob

#じゃんけんのプレイヤーを集めたグループのクラス．
class JankenGroup(mas.AgentGroup):
    """docstring for JankenGroup."""
    def __init__(self, agents=None, name=None):
        super(JankenGroup, self).__init__(agents=agents, name=name)

#じゃんけん環境のクラス．
class JankenEnv(mas.Env):
    """docstring for JankenEnv."""
    def __init__(self, groups=None, labels=None, name=None):
        super(JankenEnv, self).__init__(groups=groups, labels=labels, name=name)

    #じゃんけんをする関数．playersはじゃんけんのプレイヤーのタプル．
    #playersに渡される二人のプレイヤーでじゃんけんを行い結果を返す．
    #Returns:
    #(プレイヤー1, 1の出したハンド, 1から見た結果), (プレイヤー2, 2の出したハンド, 2から見た結果)
    def janken(self, *players):
        #playersに何も渡されなかった場合の処理．
        if len(players) == 0:
            #ランダムに2人のプレイヤーを選択する．
            players = self.get_agents_rand(num=2)
        #playersに渡されたプレイヤーの人数が2人じゃなかった場合の処理．
        elif len(players) != 2:
            #エラー処理．
            raise mas.MasException('Length mismatch error at players.')
        #players[i].probの確率分布に従って出すハンドを決定する．
        #hands[i]: {0: グー, 1: チョキ, 2: パー}
        hands = self.get_hand(players[0]), self.get_hand(players[1])
        #じゃんけん結果をNoneで初期化する．
        #res[i]: {0: 負け, 1: 勝ち, 2: 引き分け}
        res = None
        #プレイヤー1がグー(0)でプレイヤー2がチョキ(1)の場合．
        p1_win_cond1 = hands[0] == 0 and hands[1] == 1
        #プレイヤー1がチョキ(1)でプレイヤー2がパー(2)の場合．
        p1_win_cond2 = hands[0] == 1 and hands[1] == 2
        #プレイヤー1がパー(2)でプレイヤー2がグー(0)の場合．
        p1_win_cond3 = hands[0] == 2 and hands[1] == 0
        #引き分けの場合．
        if hands[0] == hands[1]:
            #両方の結果に引き分け(2)を代入する．
            res = [2, 2]
        #プレイヤー1が勝った場合．
        elif p1_win_cond1 or p1_win_cond2 or p1_win_cond3:
            #プレイヤー1のスコアをインクリメントする．
            players[0].score += 1
            #プレイヤー2のスコアをデクリメントする．
            players[1].score -= 1
            #プレイヤー1の結果に勝ち(1)を，プレイヤー2の結果に負け(0)を代入する．
            res = [1, 0]
        #プレイヤー2が買った場合．
        else:
            #プレイヤー1のスコアをデクリメントする．
            players[0].score -= 1
            #プレイヤー2のスコアをインクリメントする．
            players[1].score += 1
            #プレイヤー1の結果に負け(0)を，プレイヤー2の結果に勝ち(1)を代入する．
            res = [0, 1]
        #プレイヤー, ハンド, 結果それぞれの配列をzipして返却する．
        return zip(players, hands, res)

    #渡されたplayerのハンドをplayerの確率分布player.probに従ってランダムに決める．
    #Returns: 0-2  {0: グー, 1: チョキ, 2: パー}
    def get_hand(self, player):
        #分布の合計が1になるようにplayer.probを修正する．
        prob = [p/sum(player.prob) for p in player.prob]
        #範囲[0, 1)の乱数を生成する．
        r = random.random()
        #合計確率に0を代入
        total_prob = 0.
        #probをfor文で回してtotal_probがrを超えたときのインデックスを返却している．
        #これにより，probの確率分布に従ったハンドを求めることができる．
        for i, p in enumerate(prob):
            #totol_probにハンドiの確率pを追加する．
            total_prob += p
            #もしr < total_probならば，ハンドiを返却する．
            if r < total_prob:
                return i

#このファイルのスクリプトが直接実行された場合の処理．
#ターミナルから >python janken.py が実行された場合のみ実行される．
#このファイルがインポートされた場合には実行されない．
if __name__ == '__main__':
    #処理の開始時刻を取得
    start_time = time.time()

    #学習なしのプレイヤーグループの確率分布を決定する．
    prob1 = (0.55, 0.3, 0.15)
    #学習なしのプレイヤーのリストを生成する．プレイヤー数: 100人．
    rand_players = [Player(list(prob1), 0) for _ in range(100)]
    #学習なしのプレイヤーのグループを作成する．
    rand_group = JankenGroup(agents=rand_players)
    #学習ありのプレイヤーグループの確率分布を決定する．
    prob2 = (1./3, 1./3, 1./3)
    #学習ありのプレイヤーのリストを生成する．プレイヤー数: 100人．
    rein_players = [ReinPlayer(list(prob2), 0) for _ in range(100)]
    #学習ありのプレイヤーのグループを作成する．
    rein_group = JankenGroup(agents=rein_players)
    #2つのグループのラベルを決定する．
    labels = ['rand_group', 'rein_group']
    #2つのグループを有する環境を生成する．
    jan_env = JankenEnv(groups=[rand_group, rein_group], labels=labels)
    #一人当たりのじゃんけん回数を決定する．
    times = 100
    #じゃんけん回数 times 回繰り返す．
    for _ in range(times):
        #環境 jan_env 内のすべてのグループを取り出す（イテレート）．
        for group in jan_env:
            #グループ group 内のすべてのエージェント（プレイヤー）を取り出す（イテレート）．
            for agent in group:
                #対戦相手のプレイヤーをランダムに決定する．
                oppo_agent = jan_env.get_agents_rand(excep=agent)[0]
                #agent と oppo_agent でじゃんけんをする．
                results = jan_env.janken(agent, oppo_agent)
                #results の中身を取り出す．
                #p: プレイヤー（PlayerまたはReinPlayerのインスタンス）
                #h: ハンド(0~2)  {0: グー, 1: チョキ, 2: パー}
                #r: じゃんけんの結果(0~2)  {0: 負け, 1: 勝ち, 2: 引き分け}
                for p, h, r in results:
                    #プレイヤー p が学習ありのエージェントかどうかを判定する．
                    if jan_env.rein_group.is_existing_agent(p.get_no()):
                        #プレイヤー p がハンドとじゃんけんの結果をもとに学習する．
                        p.rein_learn(h, r)

    #100回繰り返した後の学習ありのプレイヤーの確率分布の平均．
    print('100回繰り返した後の学習ありのプレイヤーの確率分布の平均')
    print('[グーの確率, チョキの確率, パーの確率]')
    print([sum(a.prob[i] for a in jan_env.rein_group)/len(jan_env.rein_group) for i in range(3)])
    print('----------')
    #100回繰り返した後の学習ありのプレイヤーのスコアの平均．
    print('100回繰り返した後の学習ありのプレイヤーのスコアの平均')
    print(sum(a.score for a in jan_env.rein_group)/float(len(jan_env.rein_group)))
    print('----------')
    #処理の実行時間
    print('elapsed time: {} [s]'.format(time.time() - start_time))
