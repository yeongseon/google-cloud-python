# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Accesses the google.cloud.texttospeech.v1beta1 TextToSpeech API."""

import pkg_resources

import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.grpc_helpers

from google.cloud.texttospeech_v1beta1.gapic import enums
from google.cloud.texttospeech_v1beta1.gapic import text_to_speech_client_config
from google.cloud.texttospeech_v1beta1.proto import cloud_tts_pb2

_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    'google-cloud-texttospeech', ).version


class TextToSpeechClient(object):
    """Service that implements Google Cloud Text-to-Speech API."""

    SERVICE_ADDRESS = 'texttospeech.googleapis.com:443'
    """The default address of the service."""

    # The scopes needed to make gRPC calls to all of the methods defined in
    # this service
    _DEFAULT_SCOPES = ('https://www.googleapis.com/auth/cloud-platform', )

    # The name of the interface for this client. This is the key used to find
    # method configuration in the client_config dictionary.
    _INTERFACE_NAME = 'google.cloud.texttospeech.v1beta1.TextToSpeech'

    def __init__(self,
                 channel=None,
                 credentials=None,
                 client_config=text_to_speech_client_config.config,
                 client_info=None):
        """Constructor.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            client_config (dict): A dictionary of call options for each
                method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                'The `channel` and `credentials` arguments to {} are mutually '
                'exclusive.'.format(self.__class__.__name__), )

        # Create the channel.
        if channel is None:
            channel = google.api_core.grpc_helpers.create_channel(
                self.SERVICE_ADDRESS,
                credentials=credentials,
                scopes=self._DEFAULT_SCOPES,
            )

        # Create the gRPC stubs.
        self.text_to_speech_stub = (cloud_tts_pb2.TextToSpeechStub(channel))

        if client_info is None:
            client_info = (
                google.api_core.gapic_v1.client_info.DEFAULT_CLIENT_INFO)
        client_info.gapic_version = _GAPIC_LIBRARY_VERSION

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config['interfaces'][self._INTERFACE_NAME], )

        # Write the "inner API call" methods to the class.
        # These are wrapped versions of the gRPC stub methods, with retry and
        # timeout configuration applied, called by the public methods on
        # this class.
        self._list_voices = google.api_core.gapic_v1.method.wrap_method(
            self.text_to_speech_stub.ListVoices,
            default_retry=method_configs['ListVoices'].retry,
            default_timeout=method_configs['ListVoices'].timeout,
            client_info=client_info,
        )
        self._synthesize_speech = google.api_core.gapic_v1.method.wrap_method(
            self.text_to_speech_stub.SynthesizeSpeech,
            default_retry=method_configs['SynthesizeSpeech'].retry,
            default_timeout=method_configs['SynthesizeSpeech'].timeout,
            client_info=client_info,
        )

    # Service calls
    def list_voices(self,
                    language_code=None,
                    retry=google.api_core.gapic_v1.method.DEFAULT,
                    timeout=google.api_core.gapic_v1.method.DEFAULT,
                    metadata=None):
        """
        Returns a list of ``Voice``
        supported for synthesis.

        Example:
            >>> from google.cloud import texttospeech_v1beta1
            >>>
            >>> client = texttospeech_v1beta1.TextToSpeechClient()
            >>>
            >>> response = client.list_voices()

        Args:
            language_code (str): Optional (but recommended)
                `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`_ language tag. If
                specified, the ListVoices call will only return voices that can be used to
                synthesize this language_code. E.g. when specifying \"en-NZ\", you will get
                supported \"en-*\" voices; when specifying \"no\", you will get supported
                \"no-*\" (Norwegian) and \"nb-*\" (Norwegian Bokmal) voices; specifying \"zh\"
                will also get supported \"cmn-*\" voices; specifying \"zh-hk\" will also get
                supported \"yue-*\" voices.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.texttospeech_v1beta1.types.ListVoicesResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        request = cloud_tts_pb2.ListVoicesRequest(
            language_code=language_code, )
        return self._list_voices(
            request, retry=retry, timeout=timeout, metadata=metadata)

    def synthesize_speech(self,
                          input_,
                          voice,
                          audio_config,
                          retry=google.api_core.gapic_v1.method.DEFAULT,
                          timeout=google.api_core.gapic_v1.method.DEFAULT,
                          metadata=None):
        """
        Synthesizes speech synchronously: receive results after all text input
        has been processed.

        Example:
            >>> from google.cloud import texttospeech_v1beta1
            >>>
            >>> client = texttospeech_v1beta1.TextToSpeechClient()
            >>>
            >>> # TODO: Initialize ``input_``:
            >>> input_ = {}
            >>>
            >>> # TODO: Initialize ``voice``:
            >>> voice = {}
            >>>
            >>> # TODO: Initialize ``audio_config``:
            >>> audio_config = {}
            >>>
            >>> response = client.synthesize_speech(input_, voice, audio_config)

        Args:
            input_ (Union[dict, ~google.cloud.texttospeech_v1beta1.types.SynthesisInput]): Required. The Synthesizer requires either plain text or SSML as input.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.texttospeech_v1beta1.types.SynthesisInput`
            voice (Union[dict, ~google.cloud.texttospeech_v1beta1.types.VoiceSelectionParams]): Required. The desired voice of the synthesized audio.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.texttospeech_v1beta1.types.VoiceSelectionParams`
            audio_config (Union[dict, ~google.cloud.texttospeech_v1beta1.types.AudioConfig]): Required. The configuration of the synthesized audio.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.texttospeech_v1beta1.types.AudioConfig`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.texttospeech_v1beta1.types.SynthesizeSpeechResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        request = cloud_tts_pb2.SynthesizeSpeechRequest(
            input=input_,
            voice=voice,
            audio_config=audio_config,
        )
        return self._synthesize_speech(
            request, retry=retry, timeout=timeout, metadata=metadata)
