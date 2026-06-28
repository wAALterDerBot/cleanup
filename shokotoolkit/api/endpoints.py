"""
Shoko API endpoint definitions.
"""

API_PREFIX = "/api/v3"

# System
SYSTEM_STATUS = f"{API_PREFIX}/System/Status"
SYSTEM_VERSION = f"{API_PREFIX}/System/Version"

# Authentication
AUTH = f"{API_PREFIX}/Auth"

# Library
SERIES = f"{API_PREFIX}/Series"
FILES = f"{API_PREFIX}/File"
EPISODES = f"{API_PREFIX}/Episode"

# Release Management
RELEASE = f"{API_PREFIX}/Action/Release"
