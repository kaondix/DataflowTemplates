# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command to get a hyperparameter tuning job in AI platform."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.ai.hp_tuning_jobs import client
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.ai import constants
from googlecloudsdk.command_lib.ai import endpoint_util
from googlecloudsdk.command_lib.ai import flags


@base.ReleaseTracks(base.ReleaseTrack.BETA, base.ReleaseTrack.ALPHA)
class Describe(base.DescribeCommand):
  """Get detail information about the hyperparameter tuning job by given id."""

  @staticmethod
  def Args(parser):
    flags.AddHptuningJobResourceArg(parser, 'to describe')

  def Run(self, args):
    hptuning_job_ref = args.CONCEPTS.hptuning_job.Parse()
    region = hptuning_job_ref.AsDict()['locationsId']
    with endpoint_util.AiplatformEndpointOverrides(
        version=constants.BETA_VERSION, region=region):
      response = client.HpTuningJobsClient().Get(
          hptuning_job_ref.RelativeName())
      return response
