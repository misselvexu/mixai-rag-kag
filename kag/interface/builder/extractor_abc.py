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
from abc import ABC, abstractmethod
from typing import List

from kag.interface.builder.base import BuilderComponent
from kag.builder.model.chunk import Chunk
from kag.builder.model.sub_graph import SubGraph
from knext.common.base.runnable import Input, Output


class ExtractorABC(BuilderComponent, ABC):
    """
    Abstract base class for extracting sub graphs (which contain a list of nodes and a list of edges) from chunks.

    This class defines the interface for all extractor components that are responsible for processing input data
    and generating sub graphs as output. It inherits from `BuilderComponent` and `ABC` (Abstract Base Class).
    """

    @property
    def input_types(self):
        return Chunk

    @property
    def output_types(self):
        return SubGraph

    @abstractmethod
    def invoke(self, input: Input, **kwargs) -> List[Output]:
        """
        Abstract method to invoke the extractor to process input data.

        This method must be implemented by any subclass. It is responsible for processing the input data
        and generating a list of output results, typically containing subgraphs.

        Args:
            input (Input): Input data containing name and content.
            **kwargs: Additional keyword arguments.

        Returns:
            List[Output]: A list of processed results, containing subgraph information.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError(
            f"`invoke` is not currently supported for {self.__class__.__name__}."
        )
