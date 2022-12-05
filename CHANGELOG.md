# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
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
