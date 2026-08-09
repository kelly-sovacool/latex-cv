FROM rocker/tidyverse:4

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    texlive-xetex && \
    R -s -e "install.packages(c('r-here', r-'glue', 'r-tidyverse' 'r-vitae', 'r-yaml'))"