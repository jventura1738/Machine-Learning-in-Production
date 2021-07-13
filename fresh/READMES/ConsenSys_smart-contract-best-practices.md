# Smart Contract Security Best Practices

Visit the documentation site: https://consensys.github.io/smart-contract-best-practices/


Read the docs in Chinese: https://github.com/ConsenSys/smart-contract-best-practices/blob/master/README-zh.md
Read the docs in Vietnamese: https://github.com/ConsenSys/smart-contract-best-practices/blob/master/README-vi.md

## Contributions are welcome!

Feel free to submit a pull request, with anything from small fixes, to full new sections. If you are writing new content, please reference the [contributing](./docs/about/contributing.md) page for guidance on style. 

See the [issues](https://github.com/ConsenSys/smart-contract-best-practices/issues) for topics that need to be covered or updated. If you have an idea you'd like to discuss, please chat with us in [Gitter](https://gitter.im/ConsenSys/smart-contract-best-practices).

If you've written an article or blog post, please add it to the [bibliography](./docs/bibliography.md).  

## Building the documentation site

```
git clone git@github.com:ConsenSys/smart-contract-best-practices.git
cd smart-contract-best-practices
pip install -r requirements.txt
mkdocs build 
```

You can also use the `mkdocs serve` command to view the site on localhost, and live reload whenever you save changes.

## Redeploying the documentation site

```
mkdocs gh-deploy
```

