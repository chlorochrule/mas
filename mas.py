#-*- coding: utf-8 -*-
#mas v1.0.0
import random
from functools import reduce


class MasException(Exception):
    """Original MasException."""
    def __init__(self, e):
        super(MasException, self).__init__(e)


class Mas(object):
    """Base class of Agent, AgentGroup, Env."""
    __no = 0
    def __init__(self, cls):
        super(Mas, self).__init__()
        self.__no = cls.__no_countup()
        self.name = self.__class__.__name__ + str(self.__no)

    @classmethod
    def __no_countup(cls):
        cls.__no += 1
        return cls.__no

    def get_no(self):
        return self.__no


class Agent(Mas):
    """Base class of Specialized Agent class."""
    def __init__(self, name=None):
        super(Agent, self).__init__(Agent)
        if name is not None:
            self.name = name


class AgentGroup(Mas):
    """Base class of Specialized AgentGroup class."""
    def __init__(self, agents=None, name=None):
        super(AgentGroup, self).__init__(AgentGroup)
        self.agents = []
        self.removed_agents = []
        if name is not None:
            self.name = name
        self.__label = self.name
        if agents is not None:
            self.add_agent(agents)

    def __iter__(self):
        return self.agents.__iter__()

    def __len__(self):
        return len(self.agents)

    def set_label(self, label):
        self.__label = label

    def get_label(self):
        return self.__label

    def add_agent(self, agents):
        if isinstance(agents, (list, tuple)):
            for agent in agents:
                self._append_agent(agent)
        else:
            self._append_agent(agents)

    def _append_agent(self, agent):
        if isinstance(agent, Agent):
            self.agents.append(agent)
        else:
            raise TypeError('Object is not an instance of Agent.')

    def remove_agent(self, agents):
        if isinstance(agents, (list, tuple)):
            for agent in agents:
                self._remove_agent(agent)
        else:
            self._remove_agent(agents)

    def _remove_agent(self, agent):
        if isinstance(agent, Agent):
            self.agents = [a for a in self if a.get_no() != agent.get_no()]
            self.removed_agents.append(agent)
        else:
            raise TypeError('Object is not an instance of Agent.')

    def is_existing_agent(self, agent_no):
        if isinstance(agent_no, (list, tuple)):
            for i in agent_no:
                if i not in agent_no:
                    return False
            return True
        else:
            return agent_no in self.get_all_agent_no()

    def get_all_agent_no(self, excep=None):
        no_list = [agent.get_no() for agent in self]
        if excep is None:
            return no_list
        elif isinstance(excep, (list, tuple)):
            excep_no = [e.get_no() for e in excep]
            return [n for n in no_list if n not in excep_no]
        else:
            return [n for n in no_list if n != excep.get_no()]

    def get_all_agents(self, excep=None):
        if excep is None:
            return self.agents
        elif isinstance(excep, (list, tuple)):
            excep_no = [e.get_no() for e in excep]
            return [a for a in self if a.get_no() not in excep_no]
        else:
            return [a for a in self if a.get_no() != excep.get_no()]

    def get_agents_rand(self, num=1, excep=None):
        agents_list = self.get_all_agents(excep=None)
        random.shuffle(agents_list)
        return agents_list[:num]


class Env(Mas):
    """Base class of Specialized Environment class."""
    def __init__(self, groups=None, labels=None, name=None):
        super(Env, self).__init__(Env)
        self.removed_groups = []
        self.groups = []
        if name is not None:
            self.name = name
        if groups is not None:
            self.add_group(groups, labels=labels)

    def __iter__(self):
        return self.groups.__iter__()

    def __len__(self):
        return len(self.groups)

    def set_label(self, group, label):
        try:
            delattr(self, group.get_label())
        except AttributeError:
            pass
        group.set_label(label)
        setattr(self, label, group)

    def add_group(self, groups, labels=None):
        if isinstance(groups, (list, tuple)):
            for group, label in zip(groups, labels):
                self._append_group(group, label)
        else:
            self._append_group(groups, label)

    def _append_group(self, group, label=None):
        if isinstance(group, AgentGroup):
            self.groups.append(group)
            if label is None:
                label = group.get_label()
            group.set_label(label)
            self.set_label(group, label)
        else:
            raise TypeError('Object is not an instance of AgentGroup.')

    def remove_group(self, groups):
        if isinstance(groups, (list, tuple)):
            for group in groups:
                self._remove_group(group)
        else:
            self._remove_group(groups)

    def _remove_group(self, group):
        if isinstance(group, AgentGroup):
            self.groups = [g for g in self if g.get_no() != group.get_no()]
            self.removed_groups.append(group)
            delattr(self, group.get_label())
        else:
            raise TypeError('Object is not an instance of AgentGroup.')

    def is_existing_group(self, group_no):
        if isinstance(groups, (list, tuple)):
            for i in group_no:
                if i not in group_no:
                    return False
            return True
        else:
            return group_no in self.get_all_group_no()

    def get_all_group_no(self, excep=None):
        no_list = [group.get_no() for group in self]
        if excep is None:
            return no_list
        elif isinstance(excep, (list, tuple)):
            excep_no = [e.get_no() for e in excep]
            return [n for n in no_list if n not in excep_no]
        else:
            return [n for n in no_list if n != excep.get_no()]

    def get_all_groups(self, excep=None):
        if excep is None:
            return self.groups
        elif isinstance(excep, (list, tuple)):
            excep_no = [e.get_no() for e in excep]
            return [g for g in self if g.get_no() not in excep_no]
        else:
            return [g for g in self if g.get_no() != excep.get_no()]

    def get_all_agents(self, excep=None):
        agents_list = [group.agents for group in self]
        agents_list = reduce(lambda x, y: x+y, agents_list)
        if excep is None:
            return agents_list
        elif isinstance(excep, (list, tuple)):
            excep_no = [e.get_no() for e in excep]
            return [a for a in agents_list if a.get_no() not in excep_no]
        else:
            return [a for a in agents_list if a.get_no() != excep.get_no()]

    def get_agents_rand(self, num=1, excep=None):
        agents_list = self.get_all_agents(excep)
        random.shuffle(agents_list)
        return agents_list[:num]
