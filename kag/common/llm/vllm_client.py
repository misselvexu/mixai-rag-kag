# -*- coding: utf-8 -*-
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.


import json
import logging
import requests
from kag.interface import LLMClient


# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@LLMClient.register("vllm")
class VLLMClient(LLMClient):
    """
    A client class for interacting with a language model deployed by VLLM.

    This class provides methods to make synchronous requests to the VLLM server, handle model calls, and parse responses.
    """

    def __init__(self, model: str, base_url: str):
        """
        Initializes the VLLMClient instance.

        Args:
            model (str): The model to use for requests.
            base_url (str): The base URL for the VLLM API.
        """
        self.model = model
        self.base_url = base_url
        self.param = {}
        self.check()

    def sync_request(self, prompt):
        """
        Makes a synchronous request to the VLLM API with the given prompt.

        Args:
            prompt: The prompt to send to the VLLM API.

        Returns:
            str: The content of the response from the VLLM API.
        """
        self.param["messages"] = prompt
        self.param["model"] = self.model

        response = requests.post(
            self.base_url,
            data=json.dumps(self.param),
            headers={"Content-Type": "application/json"},
        )

        data = response.json()
        content = data["choices"][0]["message"]["content"]
        content = content.replace("&rdquo;", "”").replace("&ldquo;", "“")
        content = content.replace("&middot;", "")
        return content

    def __call__(self, prompt):
        """
        Executes a model request when the object is called and returns the result.

        Parameters:
            prompt (str): The prompt provided to the model.

        Returns:
            str: The response content generated by the model.
        """

        content = [{"role": "user", "content": prompt}]
        return self.sync_request(content)

    def call_with_json_parse(self, prompt):
        """
        Calls the model and attempts to parse the response into JSON format.

        Parameters:
            prompt (str): The prompt provided to the model.

        Returns:
            Union[dict, str]: If the response is valid JSON, returns the parsed dictionary; otherwise, returns the original response.
        """

        content = [{"role": "user", "content": prompt}]
        rsp = self.sync_request(content)
        _end = rsp.rfind("```")
        _start = rsp.find("```json")
        if _end != -1 and _start != -1:
            json_str = rsp[_start + len("```json") : _end].strip()
        else:
            json_str = rsp
        try:
            json_result = json.loads(json_str)
        except:
            return rsp
        return json_result
