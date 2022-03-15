#
# judge.py
#
# Copyright 2022 OTSUKI Takashi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""judge module."""
from __future__ import annotations

from typing import TypedDict

from aiwolf.agent import Agent, Species
from aiwolf.constant import Constant as C


class _Judge(TypedDict):
    agent: int
    day: int
    target: int
    result: str


class Judge:
    """The judgement whether the player is a human or a werewolf."""

    def __init__(self, agent: Agent = C.AGENT_NONE, day: int = -1, target: Agent = C.AGENT_NONE, result: Species = Species.UNC) -> None:
        """Initialize a new instance of Judge.

        Args:
            agent(optional): The agent that judged. Defaults to C.AGENT_NONE.
            day(optional): The date of the judgement. Defaults to -1.
            target(optional): The judged agent. Defaults to C.AGENT_NONE.
            result(optional): The result of the judgement. Defaults to Species.UNC.
        """
        self._agent: Agent = agent
        self._day: int = day
        self._target: Agent = target
        self._result: Species = result

    @staticmethod
    def compile(judge: _Judge) -> Judge:
        """Convert a _Judge into the corresponding Judge.

        Args:
            judge: The _Judge to be converted.

        Returns:
            The Judge converted from the given _Judge.
        """
        j: Judge = Judge()
        j._agent = Agent(judge['agent'])
        j._day = judge['day']
        j._target = Agent(judge['target'])
        j._result = Species[judge['result']]
        return j

    @property
    def agent(self) -> Agent:
        """The agent that judged."""
        return self._agent

    @property
    def day(self) -> int:
        """The date of the judgement."""
        return self._day

    @property
    def target(self) -> Agent:
        """The judged agent."""
        return self._target

    @property
    def result(self) -> Species:
        """The result of the judgement."""
        return self._result
