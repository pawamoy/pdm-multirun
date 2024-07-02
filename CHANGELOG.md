# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [1.1.1](https://github.com/pawamoy/pdm-multirun/releases/tag/1.1.1) - 2024-07-02

<small>[Compare with 1.1.0](https://github.com/pawamoy/pdm-multirun/compare/1.1.0...1.1.1)</small>

### Bug Fixes

- Support PDM 2.16 API ([181f9f2](https://github.com/pawamoy/pdm-multirun/commit/181f9f23bec9d492f8e6d0144e2c512036e6150f) by Pierre Marijon). [Issue-11](https://github.com/pawamoy/pdm-multirun/issues/11), [PR-12](https://github.com/pawamoy/pdm-multirun/pull/12)

## [1.1.0](https://github.com/pawamoy/pdm-multirun/releases/tag/1.1.0) - 2023-09-21

<small>[Compare with 1.0.0](https://github.com/pawamoy/pdm-multirun/compare/1.0.0...1.1.0)</small>

### Features

- Add `PDM_MULTIRUN_CURRENT` environment variable ([a0c1b18](https://github.com/pawamoy/pdm-multirun/commit/a0c1b18c5972cb9977702f712ec7a47b1ca14b9a) by Dom Weldon). [PR #5](https://github.com/pawamoy/pdm-multirun/pull/5)

## [1.0.0](https://github.com/pawamoy/pdm-multirun/releases/tag/1.0.0) - 2023-08-20

<small>[Compare with 0.4.0](https://github.com/pawamoy/pdm-multirun/compare/0.4.0...1.0.0)</small>

### Features

- Support environment variable to always use venvs: `PDM_MULTIRUN_USE_VENVS=1` ([16c647c](https://github.com/pawamoy/pdm-multirun/commit/16c647cf3a02f605e41282184ecbfa10c07541cf) by Dom Weldon). [Issue #4](https://github.com/pawamoy/pdm-multirun/issues/4), [PR #3](https://github.com/pawamoy/pdm-multirun/pull/3)

## [0.4.0](https://github.com/pawamoy/pdm-multirun/releases/tag/0.4.0) - 2023-06-26

<small>[Compare with 0.3.1](https://github.com/pawamoy/pdm-multirun/compare/0.3.1...0.4.0)</small>

### Breaking Changes

- Drop support for Python 3.7 (EOL 2023/06/27)

### Features

- Add support for virtual environments ([f2b8381](https://github.com/pawamoy/pdm-multirun/commit/f2b838145624ecaa245681e5e4e9ef15834f55a3) by Timothée Mazzucotelli). [Issue #1](https://github.com/pawamoy/pdm-multirun/issues/1)

## [0.3.1](https://github.com/pawamoy/pdm-multirun/releases/tag/0.3.1) - 2023-06-13

<small>[Compare with 0.3.0](https://github.com/pawamoy/pdm-multirun/compare/0.3.0...0.3.1)</small>

### Bug Fixes

- Support PDM 2.7.4 ([2cd1d14](https://github.com/pawamoy/pdm-multirun/commit/2cd1d14d2c9ce02033817543a2d0216135e7ad51) by Timothée Mazzucotelli).

## [0.3.0](https://github.com/pawamoy/pdm-multirun/releases/tag/0.3.0) - 2023-06-08

<small>[Compare with 0.2.0](https://github.com/pawamoy/pdm-multirun/compare/0.2.0...0.3.0)</small>

### Features

- Add `fail-fast` option ([8ca1604](https://github.com/pawamoy/pdm-multirun/commit/8ca1604bbbf5eb27d86d653591004a83ee294dff) by Timothée Mazzucotelli).

## [0.2.0](https://github.com/pawamoy/pdm-multirun/releases/tag/0.2.0) - 2022-12-05

<small>[Compare with 0.1.0](https://github.com/pawamoy/pdm-multirun/compare/0.1.0...0.2.0)</small>

### Features
- Set `PDM_MULTIRUN=1` when running ([67146bd](https://github.com/pawamoy/pdm-multirun/commit/67146bd4f688e41786041e31be92d31bf75a700d) by Timothée Mazzucotelli).

### Bug Fixes
- Fix splitting `PDM_MULTIRUN_VERSIONS` environment variable ([d560a99](https://github.com/pawamoy/pdm-multirun/commit/d560a99a244f82dccdee003c20d7544cbbf196fc) by Timothée Mazzucotelli).


## [0.1.0](https://github.com/pawamoy/pdm-multirun/releases/tag/0.1.0) - 2022-12-05

<small>[Compare with first commit](https://github.com/pawamoy/pdm-multirun/compare/c4b669df4a88ebaf1ad873b673133ef869139cea...0.1.0)</small>

### Features
- Support passing versions with `--versions` ([5fd48a0](https://github.com/pawamoy/pdm-multirun/commit/5fd48a0550f295e591186ded9e1ffaff7432b2a2) by Timothée Mazzucotelli).
- Support space and comma separated values for `PDM_MULTIRUN_VERSIONS` ([77aa991](https://github.com/pawamoy/pdm-multirun/commit/77aa9911fb15d72054e99023de789a7a9fbeb094) by Timothée Mazzucotelli).
- First version ([c4b669d](https://github.com/pawamoy/pdm-multirun/commit/c4b669df4a88ebaf1ad873b673133ef869139cea) by Timothée Mazzucotelli).

### Bug Fixes
- Unset cached environment earlier ([a42c2ed](https://github.com/pawamoy/pdm-multirun/commit/a42c2edfeff20b0ec22f1818d9c522269778cbbc) by Timothée Mazzucotelli).

### Code Refactoring
- Expect only versions on the CLI ([b68001f](https://github.com/pawamoy/pdm-multirun/commit/b68001f141b3f4ce32b7ceea4ac5a4ba89132cd8) by Timothée Mazzucotelli).
