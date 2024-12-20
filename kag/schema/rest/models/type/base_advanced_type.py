# coding: utf-8
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


"""
    kag

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kag.common.rest.configuration import Configuration


class BaseAdvancedType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "basic_info": "StandardTypeBasicInfo",
        "parent_type_info": "ParentTypeInfo",
        "spg_type_enum": "str",
        "properties": "list[Property]",
        "relations": "list[Relation]",
        "advanced_config": "SpgTypeAdvancedConfig",
        "project_id": "int",
        "ontology_id": "OntologyId",
        "alter_operation": "str",
        "ext_info": "object",
    }

    attribute_map = {
        "basic_info": "basicInfo",
        "parent_type_info": "parentTypeInfo",
        "spg_type_enum": "spgTypeEnum",
        "properties": "properties",
        "relations": "relations",
        "advanced_config": "advancedConfig",
        "project_id": "projectId",
        "ontology_id": "ontologyId",
        "alter_operation": "alterOperation",
        "ext_info": "extInfo",
    }

    discriminator_value_class_map = {
        "STANDARD_TYPE": "StandardType",
        "ENTITY_TYPE": "EntityType",
        "EVENT_TYPE": "EventType",
        "CONCEPT_TYPE": "ConceptType",
    }

    def __init__(
        self,
        basic_info=None,
        parent_type_info=None,
        spg_type_enum=None,
        properties=None,
        relations=None,
        advanced_config=None,
        project_id=None,
        ontology_id=None,
        alter_operation=None,
        ext_info=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """BaseAdvancedType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._basic_info = None
        self._parent_type_info = None
        self._spg_type_enum = None
        self._properties = None
        self._relations = None
        self._advanced_config = None
        self._project_id = None
        self._ontology_id = None
        self._alter_operation = None
        self._ext_info = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if parent_type_info is not None:
            self.parent_type_info = parent_type_info
        if spg_type_enum is not None:
            self.spg_type_enum = spg_type_enum
        if properties is not None:
            self.properties = properties
        if relations is not None:
            self.relations = relations
        if advanced_config is not None:
            self.advanced_config = advanced_config
        if project_id is not None:
            self.project_id = project_id
        if ontology_id is not None:
            self.ontology_id = ontology_id
        if alter_operation is not None:
            self.alter_operation = alter_operation
        if ext_info is not None:
            self.ext_info = ext_info

    @property
    def basic_info(self):
        """Gets the basic_info of this BaseAdvancedType.  # noqa: E501


        :return: The basic_info of this BaseAdvancedType.  # noqa: E501
        :rtype: StandardTypeBasicInfo
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this BaseAdvancedType.


        :param basic_info: The basic_info of this BaseAdvancedType.  # noqa: E501
        :type: StandardTypeBasicInfo
        """

        self._basic_info = basic_info

    @property
    def parent_type_info(self):
        """Gets the parent_type_info of this BaseAdvancedType.  # noqa: E501


        :return: The parent_type_info of this BaseAdvancedType.  # noqa: E501
        :rtype: ParentTypeInfo
        """
        return self._parent_type_info

    @parent_type_info.setter
    def parent_type_info(self, parent_type_info):
        """Sets the parent_type_info of this BaseAdvancedType.


        :param parent_type_info: The parent_type_info of this BaseAdvancedType.  # noqa: E501
        :type: ParentTypeInfo
        """

        self._parent_type_info = parent_type_info

    @property
    def spg_type_enum(self):
        """Gets the spg_type_enum of this BaseAdvancedType.  # noqa: E501


        :return: The spg_type_enum of this BaseAdvancedType.  # noqa: E501
        :rtype: str
        """
        return self._spg_type_enum

    @spg_type_enum.setter
    def spg_type_enum(self, spg_type_enum):
        """Sets the spg_type_enum of this BaseAdvancedType.


        :param spg_type_enum: The spg_type_enum of this BaseAdvancedType.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "BASIC_TYPE",
            "ENTITY_TYPE",
            "CONCEPT_TYPE",
            "EVENT_TYPE",
            "STANDARD_TYPE",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and spg_type_enum not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `spg_type_enum` ({0}), must be one of {1}".format(  # noqa: E501
                    spg_type_enum, allowed_values
                )
            )

        self._spg_type_enum = spg_type_enum

    @property
    def properties(self):
        """Gets the properties of this BaseAdvancedType.  # noqa: E501


        :return: The properties of this BaseAdvancedType.  # noqa: E501
        :rtype: list[Property]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this BaseAdvancedType.


        :param properties: The properties of this BaseAdvancedType.  # noqa: E501
        :type: list[Property]
        """

        self._properties = properties

    @property
    def relations(self):
        """Gets the relations of this BaseAdvancedType.  # noqa: E501


        :return: The relations of this BaseAdvancedType.  # noqa: E501
        :rtype: list[Relation]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this BaseAdvancedType.


        :param relations: The relations of this BaseAdvancedType.  # noqa: E501
        :type: list[Relation]
        """

        self._relations = relations

    @property
    def advanced_config(self):
        """Gets the advanced_config of this BaseAdvancedType.  # noqa: E501


        :return: The advanced_config of this BaseAdvancedType.  # noqa: E501
        :rtype: SpgTypeAdvancedConfig
        """
        return self._advanced_config

    @advanced_config.setter
    def advanced_config(self, advanced_config):
        """Sets the advanced_config of this BaseAdvancedType.


        :param advanced_config: The advanced_config of this BaseAdvancedType.  # noqa: E501
        :type: SpgTypeAdvancedConfig
        """

        self._advanced_config = advanced_config

    @property
    def project_id(self):
        """Gets the project_id of this BaseAdvancedType.  # noqa: E501


        :return: The project_id of this BaseAdvancedType.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BaseAdvancedType.


        :param project_id: The project_id of this BaseAdvancedType.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def ontology_id(self):
        """Gets the ontology_id of this BaseAdvancedType.  # noqa: E501


        :return: The ontology_id of this BaseAdvancedType.  # noqa: E501
        :rtype: OntologyId
        """
        return self._ontology_id

    @ontology_id.setter
    def ontology_id(self, ontology_id):
        """Sets the ontology_id of this BaseAdvancedType.


        :param ontology_id: The ontology_id of this BaseAdvancedType.  # noqa: E501
        :type: OntologyId
        """

        self._ontology_id = ontology_id

    @property
    def alter_operation(self):
        """Gets the alter_operation of this BaseAdvancedType.  # noqa: E501


        :return: The alter_operation of this BaseAdvancedType.  # noqa: E501
        :rtype: str
        """
        return self._alter_operation

    @alter_operation.setter
    def alter_operation(self, alter_operation):
        """Sets the alter_operation of this BaseAdvancedType.


        :param alter_operation: The alter_operation of this BaseAdvancedType.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATE", "UPDATE", "DELETE"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and alter_operation not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `alter_operation` ({0}), must be one of {1}".format(  # noqa: E501
                    alter_operation, allowed_values
                )
            )

        self._alter_operation = alter_operation

    @property
    def ext_info(self):
        """Gets the ext_info of this BaseAdvancedType.  # noqa: E501


        :return: The ext_info of this BaseAdvancedType.  # noqa: E501
        :rtype: object
        """
        return self._ext_info

    @ext_info.setter
    def ext_info(self, ext_info):
        """Sets the ext_info of this BaseAdvancedType.


        :param ext_info: The ext_info of this BaseAdvancedType.  # noqa: E501
        :type: object
        """

        self._ext_info = ext_info

    def get_real_child_model(self, data):
        """Returns the child model by discriminator"""
        if "@type" in data:
            child_type = data.get("@type")
            real_child_model = self.discriminator_value_class_map.get(child_type)
            return real_child_model
        return None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BaseAdvancedType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseAdvancedType):
            return True

        return self.to_dict() != other.to_dict()