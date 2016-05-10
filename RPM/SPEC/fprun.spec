%define date  %(/bin/date +%m-%d-%Y)
%define user  %(%{__id_u} -n)
%define _prefix /home/%{user}/.usr/local
%define _topdir %(pwd)
%define buildroot %(pwd)/tmp

#EDIT THIS ONLY-----------------
%define groupid <your_unix_group_name>
#-------------------------------


#Whether normal/depends
%define modulepath modulefiles
%define debug_package %{nil}
%define compiler CC=icc CXX=icpc FC=ifort F77=ifort
%define default_module 1
%define lname `echo %{name}|tr '[:upper:]' '[:lower:]'`


Summary:	faprun - a fake aprun to run shell commands on independent nodes
Name:		faprun
Version:	1.0.0
Release:        1%{?dist}
Group:          CIIC/Software
License:        GPLv2+
#Source0:        %{name}-%{version}.tar.gz
#BuildRequires: pkgconfig(libidn)
#Requires: pkgconfig(libidn)
ExclusiveArch: x86_64


%description


%prep

%build
module load boost
cp %{_topdir}/SOURCES/main.cpp %{_topdir}/BUILD/
CC -std=c++11 main.cpp -o faprun





%install
module load boost
#rm -rf %{buildroot}
mkdir -p %{_prefix}/%{lname}/%{version}/{bin,lib,lib64}
cp faprun %{_prefix}/%{lname}/%{version}/bin
#MODULES
mkdir -p %{_prefix}/share/%{modulepath}/%{lname}
cp %{_topdir}/MODULES/%{version} %{_prefix}/share/%{modulepath}/%{lname}/%{version}
sed 's/VERSION/%{version}/' -i %{_prefix}/share/%{modulepath}/%{lname}/%{version}
sed "s/NAME/%{lname}/" -i %{_prefix}/share/%{modulepath}/%{lname}/%{version}
sed 's/SUMMARY/%{summary}/' -i %{_prefix}/share/%{modulepath}/%{lname}/%{version}
%if %{default_module} == 1
        echo -e '#%Module###########################################################\nset ModulesVersion "%{version}"' >  %{_prefix}/share/%{modulepath}/%{lname}/.version
%endif


%clean
rm -rf %{buildroot}
#Only if you are sure the installation doesn't need debugging!
rm -rf %{_topdir}/BUILD/*


%post
#Relink with sym link information captured from .rpm_post
if [ -f %{_prefix}/%{lname}/%{version}/.rpm_post ]; then
        cat %{_prefix}/%{lname}/%{version}/.rpm_post|awk '{print "ln -sf "$2,$1}' |xargs -0 bash -c
        rm -rf %{_prefix}/%{lname}/%{version}/.rpm_post

fi


%files
%defattr(-,%{user},-,-)
/home/smeka/.usr/local/%{name}*
/home/smeka/.usr/local/share/modulefiles/%{name}*
