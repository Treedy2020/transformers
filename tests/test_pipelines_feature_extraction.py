# Copyright 2020 The HuggingFace Team. All rights reserved.
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

import unittest

from transformers import MODEL_MAPPING, TF_MODEL_MAPPING, CLIPConfig, FeatureExtractionPipeline, LxmertConfig, pipeline
from transformers.testing_utils import is_pipeline_test, nested_simplify, require_tf, require_torch

from .test_pipelines_common import PipelineTestCaseMeta


@is_pipeline_test
class FeatureExtractionPipelineTests(unittest.TestCase, metaclass=PipelineTestCaseMeta):
    model_mapping = MODEL_MAPPING
    tf_model_mapping = TF_MODEL_MAPPING

    @require_torch
    def test_small_model_pt(self):
        feature_extractor = pipeline(
            task="feature-extraction", model="hf-internal-testing/tiny-random-distilbert", framework="pt"
        )
        outputs = feature_extractor("This is a test")
        self.assertEqual(
            nested_simplify(outputs),
            [[[0.216, 0.686, 1.908, 0.125, 1.548, -0.869, 0.78, -0.527, -1.555, -1.012, -0.08, -2.646, -1.333, 1.2, -0.529, 1.109, -0.694, 0.209, -0.986, 0.475, -0.44, -0.641, -0.409, 1.204, -1.311, 0.316, -0.08, 0.454, 0.106, 0.923, 0.745, 1.106], [1.488, -0.283, 0.691, -2.345, -0.144, -1.454, -0.535, 0.976, -1.304, 0.134, -1.707, -0.18, 0.33, 0.982, -1.026, 0.076, 1.223, 0.819, 1.437, 0.549, 0.257, 0.307, -0.304, 0.154, -0.075, -0.583, 0.157, 0.11, 0.921, -2.434, 0.739, 1.024], [-0.328, 0.284, -0.666, 1.846, 0.158, -1.723, -0.865, -0.143, 0.09, -0.517, 0.96, -0.847, -1.069, 0.099, -0.796, 0.384, 1.594, 0.764, -1.596, 0.055, -0.484, 0.208, -0.529, 0.849, 0.051, 2.725, 2.043, -0.864, -0.497, -0.866, -0.209, -0.113], [-0.628, 0.513, -0.434, -0.906, 1.02, -1.155, 1.308, -0.144, 0.861, 0.825, 2.051, 1.127, 1.513, 0.367, 0.575, 0.72, 0.471, 0.36, -0.861, -1.835, -0.026, -0.646, 1.192, -2.123, -0.759, 0.634, -0.296, -0.161, -0.633, -0.698, -1.741, -0.492], [-0.444, 0.616, -0.252, 0.594, -0.219, 0.417, -1.118, -0.088, 1.127, -1.674, 0.762, -0.156, 1.655, 0.965, -1.03, -0.853, -0.037, 1.38, -0.726, -0.469, 0.635, 0.898, -1.506, -0.519, -0.669, 0.406, 1.767, 2.215, -1.425, -1.238, -0.878, -0.137], [1.36, -0.347, -0.009, -0.146, -1.669, 0.735, -2.14, -0.82, 0.739, 0.962, 0.393, -0.371, 0.055, -1.619, -0.605, 1.487, 1.335, 0.697, 0.867, -1.043, 0.833, -1.281, -1.389, 0.815, 0.934, 0.009, 1.075, -0.37, 0.804, -0.635, -1.327, 0.671], [-0.529, 0.78, -1.844, 1.068, 0.689, 1.022, 0.282, -1.327, 0.28, 0.119, 2.389, 0.272, 0.947, 0.404, -0.84, -0.364, -1.209, 0.759, -0.953, 0.369, -0.866, -0.406, -1.054, -0.758, -0.877, 1.837, 1.59, 0.338, -1.003, -0.211, -1.322, 0.42], [0.332, 1.92, 1.158, -0.218, -0.812, -0.676, 1.813, 0.185, -0.191, -0.654, 0.93, 0.845, -0.365, -1.043, -1.189, 0.503, 1.384, 0.161, -0.259, -1.295, 0.694, -1.925, 2.034, 0.57, 0.541, -0.76, 0.199, -1.324, -1.216, -0.444, -0.88, -0.016], [-0.743, -0.093, -0.205, 0.105, -1.328, -0.001, 0.461, 0.787, 0.118, -0.707, 0.101, -0.134, -1.015, 0.494, -1.198, 0.477, 1.271, 0.056, 2.37, 1.827, 1.16, 0.485, -1.197, -0.191, -0.113, -0.012, -1.599, -0.125, 1.035, -2.789, 0.411, 0.293], [-0.612, 1.765, 0.316, -0.193, -0.349, -0.249, -0.168, 0.96, 0.037, 1.451, -0.089, 0.811, 0.166, 0.87, 0.079, 0.885, 1.08, -0.043, 0.258, 0.577, -2.287, -1.271, -2.109, 1.513, -0.846, -1.92, -0.116, 1.476, -0.279, -0.39, -0.815, -0.509], [-0.591, 0.048, -0.422, 1.068, -0.005, 1.891, 0.094, -1.655, -0.857, -0.981, 3.114, 0.789, 0.363, -1.244, -0.046, -0.964, 0.169, 0.806, -0.213, 0.566, 0.25, -0.205, -1.564, 0.263, 0.079, 0.565, 0.597, 1.045, -1.327, -0.293, 0.103, -1.443], [2.397, 1.062, -0.573, 1.594, 0.521, 0.241, 0.896, -1.182, -0.563, -0.935, -0.992, -0.655, 1.825, -1.338, -0.335, -0.868, 1.297, -0.299, 0.411, -0.638, -0.404, -1.499, 0.753, 1.012, -0.144, 0.704, -1.337, 0.454, -1.034, 0.564, -0.943, 0.008], [0.039, 1.009, 1.153, -0.478, -0.411, 0.065, -1.489, -0.562, 0.796, 0.388, -0.451, 2.051, 0.514, -0.756, 0.661, -1.563, 1.441, 0.116, 1.161, -0.769, 0.152, 0.301, -1.23, 0.185, -0.848, -1.246, 0.008, -1.513, -0.283, -0.811, 2.601, -0.233]]])  # fmt: skip

    @require_tf
    def test_small_model_tf(self):
        feature_extractor = pipeline(
            task="feature-extraction", model="hf-internal-testing/tiny-random-distilbert", framework="tf"
        )
        outputs = feature_extractor("This is a test")
        self.assertEqual(
            nested_simplify(outputs),
            [[[0.216, 0.686, 1.908, 0.125, 1.548, -0.869, 0.78, -0.527, -1.555, -1.012, -0.08, -2.646, -1.333, 1.2, -0.529, 1.109, -0.694, 0.209, -0.986, 0.475, -0.44, -0.641, -0.409, 1.204, -1.311, 0.316, -0.08, 0.454, 0.106, 0.923, 0.745, 1.106], [1.488, -0.283, 0.691, -2.345, -0.144, -1.454, -0.535, 0.976, -1.304, 0.134, -1.707, -0.18, 0.33, 0.982, -1.026, 0.076, 1.223, 0.819, 1.437, 0.549, 0.257, 0.307, -0.304, 0.154, -0.075, -0.583, 0.157, 0.11, 0.921, -2.434, 0.739, 1.024], [-0.328, 0.284, -0.666, 1.846, 0.158, -1.723, -0.865, -0.143, 0.09, -0.517, 0.96, -0.847, -1.069, 0.099, -0.796, 0.384, 1.594, 0.764, -1.596, 0.055, -0.484, 0.208, -0.529, 0.849, 0.051, 2.725, 2.043, -0.864, -0.497, -0.866, -0.209, -0.113], [-0.628, 0.513, -0.434, -0.906, 1.02, -1.155, 1.308, -0.144, 0.861, 0.825, 2.051, 1.127, 1.513, 0.367, 0.575, 0.72, 0.471, 0.36, -0.861, -1.835, -0.026, -0.646, 1.192, -2.123, -0.759, 0.634, -0.296, -0.161, -0.633, -0.698, -1.741, -0.492], [-0.444, 0.616, -0.252, 0.594, -0.219, 0.417, -1.118, -0.088, 1.127, -1.674, 0.762, -0.156, 1.655, 0.965, -1.03, -0.853, -0.037, 1.38, -0.726, -0.469, 0.635, 0.898, -1.506, -0.519, -0.669, 0.406, 1.767, 2.215, -1.425, -1.238, -0.878, -0.137], [1.36, -0.347, -0.009, -0.146, -1.669, 0.735, -2.14, -0.82, 0.739, 0.962, 0.393, -0.371, 0.055, -1.619, -0.605, 1.487, 1.335, 0.697, 0.867, -1.043, 0.833, -1.281, -1.389, 0.815, 0.934, 0.009, 1.075, -0.37, 0.804, -0.635, -1.327, 0.671], [-0.529, 0.78, -1.844, 1.068, 0.689, 1.022, 0.282, -1.327, 0.28, 0.119, 2.389, 0.272, 0.947, 0.404, -0.84, -0.364, -1.209, 0.759, -0.953, 0.369, -0.866, -0.406, -1.054, -0.758, -0.877, 1.837, 1.59, 0.338, -1.003, -0.211, -1.322, 0.42], [0.332, 1.92, 1.158, -0.218, -0.812, -0.676, 1.813, 0.185, -0.191, -0.654, 0.93, 0.845, -0.365, -1.043, -1.189, 0.503, 1.384, 0.161, -0.259, -1.295, 0.694, -1.925, 2.034, 0.57, 0.541, -0.76, 0.199, -1.324, -1.216, -0.444, -0.88, -0.016], [-0.743, -0.093, -0.205, 0.105, -1.328, -0.001, 0.461, 0.787, 0.118, -0.707, 0.101, -0.134, -1.015, 0.494, -1.198, 0.477, 1.271, 0.056, 2.37, 1.827, 1.16, 0.485, -1.197, -0.191, -0.113, -0.012, -1.599, -0.125, 1.035, -2.789, 0.411, 0.293], [-0.612, 1.765, 0.316, -0.193, -0.349, -0.249, -0.168, 0.96, 0.037, 1.451, -0.089, 0.811, 0.166, 0.87, 0.079, 0.885, 1.08, -0.043, 0.258, 0.577, -2.287, -1.271, -2.109, 1.513, -0.846, -1.92, -0.116, 1.476, -0.279, -0.39, -0.815, -0.509], [-0.591, 0.048, -0.422, 1.068, -0.005, 1.891, 0.094, -1.655, -0.857, -0.981, 3.114, 0.789, 0.363, -1.244, -0.046, -0.964, 0.169, 0.806, -0.213, 0.566, 0.25, -0.205, -1.564, 0.263, 0.079, 0.565, 0.597, 1.045, -1.327, -0.293, 0.103, -1.443], [2.397, 1.062, -0.573, 1.594, 0.521, 0.241, 0.896, -1.182, -0.563, -0.935, -0.992, -0.655, 1.825, -1.338, -0.335, -0.868, 1.297, -0.299, 0.411, -0.638, -0.404, -1.499, 0.753, 1.012, -0.144, 0.704, -1.337, 0.454, -1.034, 0.564, -0.943, 0.008], [0.039, 1.009, 1.153, -0.478, -0.411, 0.065, -1.489, -0.562, 0.796, 0.388, -0.451, 2.051, 0.514, -0.756, 0.661, -1.563, 1.441, 0.116, 1.161, -0.769, 0.152, 0.301, -1.23, 0.185, -0.848, -1.246, 0.008, -1.513, -0.283, -0.811, 2.601, -0.233]]])  # fmt: skip

    def get_shape(self, input_, shape=None):
        if shape is None:
            shape = []
        if isinstance(input_, list):
            subshapes = [self.get_shape(in_, shape) for in_ in input_]
            if all(s == 0 for s in subshapes):
                shape.append(len(input_))
            else:
                subshape = subshapes[0]
                shape = [len(input_), *subshape]
        elif isinstance(input_, float):
            return 0
        else:
            raise ValueError("We expect lists of floats, nothing else")
        return shape

    def run_pipeline_test(self, model, tokenizer, feature_extractor):
        if tokenizer is None:
            self.skipTest("No tokenizer")
            return

        elif isinstance(model.config, (LxmertConfig, CLIPConfig)):
            self.skipTest(
                "This is an Lxmert bimodal model, we need to find a more consistent way to switch on those models."
            )
            return
        elif model.config.is_encoder_decoder:
            self.skipTest(
                """encoder_decoder models are trickier for this pipeline.
                Do we want encoder + decoder inputs to get some featues?
                Do we want encoder only features ?
                For now ignore those.
                """
            )

            return

        feature_extractor = FeatureExtractionPipeline(
            model=model, tokenizer=tokenizer, feature_extractor=feature_extractor
        )

        outputs = feature_extractor("This is a test")

        shape = self.get_shape(outputs)
        self.assertEqual(shape[0], 1)

        # If we send too small input
        # there's a bug within FunnelModel (output with shape [1, 4, 2, 1] doesn't match the broadcast shape [1, 4, 2, 2])
        outputs = feature_extractor(["This is a test", "Another longer test"])
        shape = self.get_shape(outputs)
        self.assertEqual(shape[0], 2)
