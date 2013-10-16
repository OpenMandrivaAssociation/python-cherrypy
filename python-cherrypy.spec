%define tarname CherryPy-%{version}

Summary:        A Python-based framework for web application development
Name:           python-cherrypy
Version:        3.2.4
Release:        1
License:        BSD
Group:          Development/Python
URL:            http://www.cherrypy.org
Source0:        https://pypi.python.org/packages/source/C/CherryPy/CherryPy-%{version}.tar.gz
BuildRequires:	python-devel
BuildArch:      noarch

%description
A Python-based framework for web application development.

CheryPy allows you to write and easyly deploy web applications, thanks
to a bundled webserver. It features a automated way to map an url to a
mathod, allowing you to describe your site as a python class.

%prep
%setup -q -n %tarname

%build
%__python setup.py build
cat > tutorial.conf << EOF
[server]
socketPort = 8080
threadPool = 10

[session]
storageType=ram
EOF

%install
%__python setup.py install --root  %buildroot

%files
%doc README.txt
%doc cherrypy/tutorial/*
%{py_puresitedir}/cherrypy
%{py_puresitedir}/CherryPy-%{version}-py%{py_ver}.egg-info
%{_bindir}/cherryd


%changelog
* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.1.2-1mdv2010.1
+ Revision: 489397
- new version

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 3.1.1-2mdv2010.0
+ Revision: 442058
- rebuild

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 3.1.1-1mdv2009.1
+ Revision: 324269
- New upstream release

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 3.1.0-1mdv2009.0
+ Revision: 280549
- New release

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.2.1-3mdv2009.0
+ Revision: 242389
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.1-1mdv2008.0
+ Revision: 52594
- update to new version 2.2.1


* Wed Dec 20 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.1.1-2mdv2007.0
+ Revision: 100512
- Rebuild against new python

  + Michael Scherer <misc@mandriva.org>
    - Import python-cherrypy

* Tue Apr 11 2006 Michael Scherer <misc@mandriva.org> 2.1.1-1mdk
- New release 2.1.1

* Wed Jan 11 2006 Michael Scherer <misc@mandriva.org> 2.1.0-2mdk
- Use new python macro

* Fri Dec 09 2005 Michael Scherer <misc@mandriva.org> 2.1.0-1mdk
- New release 2.1.0
- use mkrel

* Mon Dec 06 2004 Michael Scherer <misc@mandrake.org> 2.0-0.0a1.1mdk 
- initial package for Mandrakelinux


