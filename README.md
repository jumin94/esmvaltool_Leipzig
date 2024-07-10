### Using ESMValTool at LIM cluster

These tools are installed under /opt/miniforge3. To use them, perform the following steps before using them for the first time:

These tools are installed under /opt/miniforge3. To be able to use them, carry out the following steps before using them for the first time:

add the following lines to ~/.bashrc:

      # >>> conda initialize >>>
      #!! Contents within this block are managed by 'conda init' !!
      __conda_setup="$('/opt/miniforge3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
      if [ $? -eq 0 ]; then
              eval "$__conda_setup"
      else
              if [ -f "/opt/miniforge3/etc/profile.d/conda.sh" ]; then
                      . "/opt/miniforge3/etc/profile.d/conda.sh"
              else
                       export PATH="/opt/miniforge3/bin:$PATH"
               fi
       fi
       unset __conda_setup
       if [ -f "/opt/miniforge3/etc/profile.d/mamba.sh" ]; then
             . "/opt/miniforge3/etc/profile.d/mamba.sh"
        fi
        # <<< conda initialize <<<

Load configuration

      . ~/.bashrc
      
Activate ESMValTool

      conda activate esmvaltool
      
Create the configuration file (will be saved to a hidden folder (.esvaltool) in your home folder

      esmvaltool config get_config_user

      
Edit the directory paths in the configuration file to match the one uploaded in this repository (config-user.yml) and upload the config-developer.yml to the same folder
      
Check the installation

      esmvaltool run examples/recipe_python.yml 
