# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"

  config.vm.provider "virtualbox" do |vb|
     vb.memory = "2048" # trust me, you will need this...
  end
  config.vm.provision "shell", inline: <<-SHELL
      yum install -yy vim python python-pip systemd-python docker
      SHELL

  config.vm.provision "shell", inline: "sysctl -w vm.max_map_count=262144" # this is for ES...
end
