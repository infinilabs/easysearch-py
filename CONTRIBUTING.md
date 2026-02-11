# Python Easysearch Client

If you have a bugfix or new feature that you would like to contribute to
easysearch-py, please find or open an issue about it first. Talk about what
you would like to do. It may be that somebody is already working on it, or that
there are particular issues that you should know about before implementing the
change.

We enjoy working with contributors to get their code accepted. There are many
approaches to fixing a problem and it is important to find the best approach
before writing too much code.

## API Code Generation

All the API methods (any method in `easysearch.client` classes decorated
with `@query_params`) are actually auto-generated from the
rest-api-spec found in the `Easysearch` repository. Any changes to those methods should be
done either by submitting a PR to Easysearch itself (in case of adding or
modifying any of the API methods) or to the Generate Script.

To run the code generation make sure you have pre-requisites installed:

* by running `pip install -e '.[develop]'`
* having the easysearch repo cloned and switched to appropriate version

Then you should be able to run the code generation by invoking:

```
$ python utils/generate_api.py
```


## Contributing Code Changes

The process for contributing to Easysearch repositories is similar to other open source projects.

1. Please make sure you have signed the Contributor License Agreement if required.

2. Run the linter and test suite to ensure your changes do not break existing code:

    ````
    # Install Nox for task management
    $ python -m pip install nox
    
    # Auto-format and lint your changes
    $ nox -s blacken
   
    # Run the test suite
    $ python setup.py test
    ````

   See the README file in `test_easysearch` directory for more information on
   running the test suite.

3. Rebase your changes.
   Update your local repository with the most recent code from the main
   easysearch-py repository, and rebase your branch on top of the latest master
   branch. We prefer your changes to be squashed into a single commit.

4. Submit a pull request. Push your local changes to your forked copy of the
   repository and submit a pull request. In the pull request, describe what your
   changes do and mention the number of the issue where discussion has taken
   place, eg “Closes #123″.  Please consider adding or modifying tests related to
   your changes.

Then sit back and wait. There will probably be a discussion about the pull
request and, if any changes are needed, we would love to work with you to get
your pull request merged into easysearch-py.
