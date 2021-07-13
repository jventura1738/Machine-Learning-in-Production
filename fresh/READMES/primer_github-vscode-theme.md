# GitHub's VS Code themes

![GitHub VS Code theme](https://user-images.githubusercontent.com/378023/114663107-c1c97e00-9d34-11eb-8aa6-0c4f3d35af0b.png)

## Install

1. Go to [VS Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.github-vscode-theme).
2. Click on the "Install" button.
3. Then [select a theme](https://code.visualstudio.com/docs/getstarted/themes#_selecting-the-color-theme). Currently the following themes are available:
    - `GitHub Light`
    - `GitHub Dark`
    - `GitHub Light Default` ✨ new ✨ 
    - `GitHub Dark Default` ✨ new ✨ 
    - `GitHub Dark Dimmed` ✨ new ✨ 

## Override this theme

To quickly test something, you can also override this (or any other) theme in your personal config file. Please follow the guide in the [color theme](https://code.visualstudio.com/api/extension-guides/color-theme) documentation.

## Contribute

1. Clone and open this [repo](https://github.com/primer/github-vscode-theme) in VS Code
2. Run `npm install` to install the Primer CSS color reference and run `npm start` to run the converter.
3. Press `F5` to open a new window with your extension loaded
4. Open `Code > Preferences > Color Theme` [`⌘k ⌘t`] and pick the "GitHub Light" or "GitHub Dark" theme
5. Make changes to the [`/src/theme.js`](https://github.com/primer/github-vscode-theme/blob/master/src/theme.js) file.
    - **UI**: For all changes to the "outer UI", like (status bar, file navigation etc.), take a look at the [Theme Color](https://code.visualstudio.com/api/references/theme-color) reference.
    - **Syntax**: For changes to the "code highlighting", examine the syntax scopes by invoking the [`Developer: Inspect Editor Tokens and Scopes`](https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide#scope-inspector) command from the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) in the Extension Development Host window.
6. Commit your changes and open a PR.

Note:

- If possible use colors from [Primer's color system](https://primer.style/css/support/color-system).
- Changes to the theme files are automatically applied to the Extension Development Host window, so no reloading should be necessary.

## Publish (internal)

> Note: Publishing a new version of this theme is only meant for maintainers.

**Prerequisite**: Please follow this [guide](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) to install and login to `vsce`. Ask an existing maintainer how to get the "Personal Access Token".

1. Merge any PR that is ready to be published into `master`.
2. Run `npm run build` to generate the themes with the new changes.
3. Update [CHANGELOG.md](https://github.com/primer/github-vscode-theme/blob/master/CHANGELOG.md) + commit the changes.
4. Run `vsce publish [version]`. Follow the [SemVer](https://semver.org) convention and replace `[version]` with one of the following  options:
    - `patch` for bug fixes
    - `minor` for improvements
    - `major` for breaking or bigger changes
5. Push the commits and make a [new release](https://github.com/primer/github-vscode-theme/releases/new).
