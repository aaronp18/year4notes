# Install and setup instrustions for running mdBook locally

Install rust.

On wsl you can use: 
`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`

`source ~/.bashrc`

Then install mdbook
`cargo install mdbook mdbook-katex`


`mdbook serve -p 8080 -n 0.0.0.0` 


# Install and Setup Instructions to run Jekyll locally (OLD)

Follow these instructions for WSL2 setup [here](https://www.vgemba.net/blog/Setup-Jekyll-WSL/).

`sudo apt update && sudo apt upgrade -y`

`sudo apt-get install -y ruby-full build-essential zlib1g-dev`

```
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```


`gem install bundler`

Manually install 
`gem install jekyll-sass-converter -v 1.5.2`

Apparently matches github pages
`gem install jekyll --version 3.8.5`


Then with project, install:

`bundle install`

Then run the server:
`bundle exec jekyll serve --watch --force_polling --incremental`

Then open the browser to `http://localhost:4000/`

