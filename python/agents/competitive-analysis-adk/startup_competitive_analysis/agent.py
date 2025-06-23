# Copyright 2025 Google LLC
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

"""Competitors_Analysis: Websearch and Competitors Analysis."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.battle_card.agent import battle_card_agent
from .sub_agents.competitors_websearch import competitors_websearch_agent

MODEL = "gemini-2.5-pro-preview-05-06"

competitors_agent = LlmAgent(
    name="competitive_analysis_coordinator_agent",
    model=MODEL,
    description=(
        "analyzing business description and pitch-decks provided by the users, "
        "providing research advice, locating current competitors "
        "relevant to the provided business description, generating battle-cards and suggestions "
        "for a unique value proposition, and accessing web resources "
        "to acquire knowledge"
    ),
    instruction=prompt.COMPETITORS_RESEARCH_PROMPT,
    output_key="business_description",
    tools=[
        AgentTool(agent=competitors_websearch_agent),
        AgentTool(agent=battle_card_agent),
    ],
)

root_agent = competitors_agent
