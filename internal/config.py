import logging

from configargparse import ArgumentParser, ArgumentDefaultsHelpFormatter, YAMLConfigFileParser


def setup_args_parser() -> ArgumentParser:
    parser = ArgumentParser(
        config_file_parser_class=YAMLConfigFileParser,
        default_config_files=['config.yml'],
        args_for_setting_config_path=['-c', '--config-file'],
        config_arg_help_message='Config file path',
        formatter_class=ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('--log-level', type=str, default=logging.DEBUG, help='Logging level')

    api_group = parser.add_argument_group('API')
    api_group.add_argument('--host', type=str, help='API host')
    api_group.add_argument('--port', type=int, help='API port')

    return parser
