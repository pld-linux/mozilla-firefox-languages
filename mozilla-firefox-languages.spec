# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=%{version}
U=http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Firefox
Summary(pl.UTF-8):	Pakiety językowe dla Firefoksa
Name:		mozilla-firefox-languages
Version:	33.1.1
Release:	1
License:	MPL v2.0
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source0-md5:	5b917445dd7a63491e09bc1d850eb48e
Source1:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source1-md5:	3300ffb7bb52eaa558a722fc4d5c381f
Source2:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source2-md5:	15a812d78e7c45d4e6a9dcf6bc9f54bf
Source3:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source3-md5:	0e10b84275f8e3d13b9b998257a65e81
Source4:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source4-md5:	85f7040b40bef3ce22695df41f09cde4
Source5:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/as.xpi
# Source5-md5:	c56d00208165c1cb7ca69942fe88cc00
Source6:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source6-md5:	01a258d79d4a3605719d5463d32bd7d1
Source7:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source7-md5:	c1789f39eabf2a1c1bf9b6ae8c2d0981
Source8:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source8-md5:	4b8c3a0261eb33ce626e5805699e61b6
Source9:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source9-md5:	13fa61ec953cc2710ce5657cb98c9363
Source10:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-IN.xpi
# Source10-md5:	6dda03a9805cde964bec5bafd4d69284
Source11:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source11-md5:	a3d8081a9c43a072f852ac773dc94ff1
Source12:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source12-md5:	019432656b00aefeb089fd34c85ac718
Source13:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source13-md5:	e4bfab40e5e9584c8ff7df71b06e80af
Source14:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source14-md5:	daa18c0e58db366b0710219c2634df31
Source15:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/csb.xpi
# Source15-md5:	c25890fdad80ab04fe8588c636f0b447
Source16:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source16-md5:	81d2061de1b220bcee035828d72843aa
Source17:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source17-md5:	b5aa46eb70f1c46526c7f3fcfe4abe07
Source18:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source18-md5:	a767c73386e5276d964c0a50e1ef7c95
Source19:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source19-md5:	3ea8c83b3c0ee893f876626ed241e997
Source20:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source20-md5:	a4212e1847be1dc4b0e5f5ef67650ad8
Source21:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source21-md5:	027311bb5bf08fc1725325ce86582c35
Source22:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source22-md5:	2eac48251794c96851e8e41243c8324f
Source23:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-ZA.xpi
# Source23-md5:	eaf1413aa0962e02660cbc2b8afdf0d1
Source24:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source24-md5:	ed677cf4559cb3b5108b291badd9d108
Source25:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source25-md5:	a27c97b0947d5e026ed93bb4dfabc79f
Source26:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source26-md5:	1e97297ea43e832677dd6bac7f31ac0b
Source27:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source27-md5:	a0d923b9232b6ce5d62082aaf6e83402
Source28:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source28-md5:	9f44dd765867046bc2a6b8dd2e6a9d14
Source29:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source29-md5:	bd18711fac14277789694fedd36af780
Source30:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source30-md5:	3aa9d63da86b241e09a40c959b317414
Source31:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source31-md5:	77614b07e6afb737b0f5377c06cba97c
Source32:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source32-md5:	22382722c51d993b982c0f9e9e86ea5d
Source33:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source33-md5:	5fb040615710687d157e55fb1bd357c1
Source34:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source34-md5:	cd91b2c4518475e7b6a1ca253e9c4375
Source35:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source35-md5:	182621cdae9968fa733a8c97628420e3
Source36:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source36-md5:	8b040d8a034bbc2fdbce375ab1e22e01
Source37:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source37-md5:	267f30675aefefd7eef9abff83e6fcc7
Source38:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source38-md5:	a25e2de58a0c8a3f4095efdcc4586b8d
Source39:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source39-md5:	faee6358186b382981a15af2cab140fd
Source40:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source40-md5:	fb7d80b235e5a6baa117b52fdda93e0e
Source41:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source41-md5:	4296de7db58d85077d35995fb2fcda8e
Source42:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source42-md5:	855fc63ba8e6e818b85d12910a57a867
Source43:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source43-md5:	43b963c8020f7fb4bac6c723cb8f90bc
Source44:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source44-md5:	f098b7bd3aefc88cfdc78f7a61ce7c3d
Source45:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source45-md5:	2c3fc1c274698acaf91d954a747a25c0
Source46:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source46-md5:	3aa769b260f7b79885e2239955421096
Source47:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source47-md5:	f8a414f1b3baa4575562f290c683ca38
Source48:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source48-md5:	c34efc34830ce70dc076aee236351a9f
Source49:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source49-md5:	89b762d07fa4702189937a504e3174d4
Source50:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source50-md5:	992b40425c70c4259c09a9d12e8af50d
Source51:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source51-md5:	7adef40f1e721811d3356191a49a1f0c
Source52:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source52-md5:	3f1f264d51854f4755e88cc50bb7e607
Source53:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source53-md5:	9eefdb64666d91473c49ef403e420df6
Source54:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ku.xpi
# Source54-md5:	88189601734da00c7e512b03c1c4e309
Source55:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source55-md5:	ec2222021ba9da00a2f92dae8528dd21
Source56:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source56-md5:	da3cf4fa4e57425ab9e7d2a3a43f103b
Source57:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source57-md5:	b17108b73991aa887869e2cf189709a3
Source58:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mai.xpi
# Source58-md5:	e30d07633ca19dd2e5901f94fb9f3338
Source59:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source59-md5:	09be26776392f970f1e54d8fc4dd6f3c
Source60:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ml.xpi
# Source60-md5:	b7a3ad4e63fd16f4df5bb48371be7281
Source61:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source61-md5:	16d2791c2d7e61768a1d5f67150dbe0c
Source62:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source62-md5:	081d25f343215a639021c72d425f741d
Source63:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source63-md5:	633d202321967071d6b9d71f403c4084
Source64:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source64-md5:	3663805dbd0d156e4df306c10cf32c80
Source65:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source65-md5:	d46d6493359daf78f5054dfd12e85a07
Source66:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/or.xpi
# Source66-md5:	d9462c792046ba65e0fcb87064d2e85f
Source67:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source67-md5:	8e0648343365ce89b7e6318a4dc12480
Source68:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source68-md5:	c53f5f7aebf22f4ca04e2165bc51b97b
Source69:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source69-md5:	1ea6e2ebf61418b24658b6f61ee372c3
Source70:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source70-md5:	1736fbfe7c987b117349bbce18c04599
Source71:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source71-md5:	7fbe1f60713bfb3602f9a3171603b4d8
Source72:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source72-md5:	b335ec8fa93a91b1293f0e90d91d3ded
Source73:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source73-md5:	b3f1be00ec52e54648f59f378e3d9316
Source74:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source74-md5:	d423c478b179aa5308130926c72af36b
Source75:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source75-md5:	c96d374c08f7b483b37b31a633ba0cf1
Source76:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source76-md5:	a0988da5eab940f3e5734b0df36cbedb
Source77:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source77-md5:	c99456ca7df13eeefeea51155a5449df
Source78:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source78-md5:	e0b793910c4433e75078e9a6a8273c45
Source79:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source79-md5:	19277d46d9e99de14d37f6387cf182a8
Source80:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source80-md5:	d9ceb4923a2a83227956edf6725979ac
Source81:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source81-md5:	0bf0bbb24df8227379165a2620a69764
Source82:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source82-md5:	bacb1f9517041091ff0e213c0504cf96
Source83:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source83-md5:	9f56a33b32acb643ad34b2eec48a53e4
Source84:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source84-md5:	758d2fd337a533a0eef7ef6667b04e68
Source85:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source85-md5:	80e48d915386111cfb41a73854184d15
Source86:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source86-md5:	0d3c88966c25dcde19999f7fce6ae2d1
Source87:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source87-md5:	b9273717d92e23afc710439e77e3c7c2
Source88:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source88-md5:	e97685011193ab5ae3ffbcb4b58dacae
Source89:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source89-md5:	c2508ed6cc31829a6cf348f74c00c67d
Source90:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zu.xpi
# Source90-md5:	19eee540e5768b2431de128a29ff87f7
URL:		http://www.mozilla.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		firefoxdir	%{_datadir}/mozilla-firefox

%description
Language packs for Firefox.

%description -l pl.UTF-8
Pakiety językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ach
Summary:	Acoli resources for Firefox
Summary(pl.UTF-8):	Pliki językowe aczoli dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ach
Acoli resources for Firefox.

%description -n mozilla-firefox-lang-ach -l pl.UTF-8
Pliki językowe aczoli dla Firefoksa.

%package -n mozilla-firefox-lang-af
Summary:	Afrikaans resources for Firefox
Summary(pl.UTF-8):	Afrykanerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-af
Afrikaans resources for Firefox.

%description -n mozilla-firefox-lang-af -l pl.UTF-8
Afrykanerskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-an
Summary:	Aragonese resources for Firefox
Summary(pl.UTF-8):	Aragońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-an
Aragonese resources for Firefox.

%description -n mozilla-firefox-lang-an -l pl.UTF-8
Aragońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ar
Summary:	Arabic resources for Firefox
Summary(pl.UTF-8):	Arabskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ar
Arabic resources for Firefox.

%description -n mozilla-firefox-lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-as
Summary:	Assamese resources for Firefox
Summary(pl.UTF-8):	Asamskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}

%description -n mozilla-firefox-lang-as
Assamese resources for Firefox.

%description -n mozilla-firefox-lang-as -l pl.UTF-8
Asamskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ast
Summary:	Asturian resources for Firefox
Summary(pl.UTF-8):	Asturyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ast
Asturian resources for Firefox.

%description -n mozilla-firefox-lang-ast -l pl.UTF-8
Asturyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-az
Summary:	Azerbaijani resources for Firefox
Summary(pl.UTF-8):	Azerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-az
Azerbaijani resources for Firefox.

%description -n mozilla-firefox-lang-az -l pl.UTF-8
Azerskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-be
Summary:	Belarusian resources for Firefox
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-be
Belarusian resources for Firefox.

%description -n mozilla-firefox-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-bg
Summary:	Bulgarian resources for Firefox
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bg
Bulgarian resources for Firefox.

%description -n mozilla-firefox-lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-bn
Summary:	Bengali (Bangladesh) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bn
Bengali (Bangladesh) resources for Firefox.

%description -n mozilla-firefox-lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu).

%package -n mozilla-firefox-lang-bn_IN
Summary:	Bengali (India) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bn_IN
Bengali (India) resources for Firefox.

%description -n mozilla-firefox-lang-bn_IN -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Indii).

%package -n mozilla-firefox-lang-br
Summary:	Breton resources for Firefox
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-br
Breton resources for Firefox.

%description -n mozilla-firefox-lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-bs
Summary:	Bosnian resources for Firefox
Summary(pl.UTF-8):	Bośniackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bs
Bosnian resources for Firefox.

%description -n mozilla-firefox-lang-bs -l pl.UTF-8
Bośniackie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ca
Summary:	Catalan resources for Firefox
Summary(ca.UTF-8):	Recursos catalans per Firefox
Summary(es.UTF-8):	Recursos catalanes para Firefox
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Firefoksa
Group:		I18n
URL:		http://www.softcatala.org/projectes/mozilla/
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ca
Catalan resources for Firefox.

%description -n mozilla-firefox-lang-ca -l ca.UTF-8
Recursos catalans per Firefox.

%description -n mozilla-firefox-lang-ca -l es.UTF-8
Recursos catalanes para Firefox.

%description -n mozilla-firefox-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-cs
Summary:	Czech resources for Firefox
Summary(pl.UTF-8):	Czeskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-cs
Czech resources for Firefox.

%description -n mozilla-firefox-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-csb
Summary:	Kashubian resources for Firefox
Summary(pl.UTF-8):	Kaszubskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-csb
Kashubian resources for Firefox.

%description -n mozilla-firefox-lang-csb -l pl.UTF-8
Kaszubskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-cy
Summary:	Welsh resources for Firefox
Summary(pl.UTF-8):	Walijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-cy
Welsh resources for Firefox.

%description -n mozilla-firefox-lang-cy -l pl.UTF-8
Walijskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-da
Summary:	Danish resources for Firefox
Summary(pl.UTF-8):	Duńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-da
Danish resources for Firefox.

%description -n mozilla-firefox-lang-da -l pl.UTF-8
Duńskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-de
Summary:	German resources for Firefox
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-de
German resources for Firefox.

%description -n mozilla-firefox-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-dsb
Summary:	Lower Sorbian resources for Firefox
Summary(pl.UTF-8):	Dolnołużyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-dsb
Lower Sorbian resources for Firefox.

%description -n mozilla-firefox-lang-dsb -l pl.UTF-8
Dolnołużyckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-el
Summary:	Greek resources for Firefox
Summary(pl.UTF-8):	Greckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-el
Greek resources for Firefox.

%description -n mozilla-firefox-lang-el -l pl.UTF-8
Greckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-en_GB
Summary:	English (British) resources for Firefox
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-en_GB
English (British) resources for Firefox.

%description -n mozilla-firefox-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-en_US
Summary:	English (American) resources for Firefox
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-en_US
English (American) resources for Firefox.

%description -n mozilla-firefox-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-en_ZA
Summary:	English (South Africa) resources for Firefox
Summary(pl.UTF-8):	Angielskie pliki językowe dla Firefoksa (wersja dla RPA)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-en_ZA
English (South Africa) resources for Firefox.

%description -n mozilla-firefox-lang-en_ZA -l pl.UTF-8
Angielskie pliki językowe dla Firefoksa (wersja dla Republiki
Południowej Afryki).

%package -n mozilla-firefox-lang-eo
Summary:	Esperanto resources for Firefox
Summary(pl.UTF-8):	Pliki językowe esperanto dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-eo
Esperanto resources for Firefox.

%description -n mozilla-firefox-lang-eo -l pl.UTF-8
Pliki językowe esperanto dla Firefoksa.

%package -n mozilla-firefox-lang-es_AR
Summary:	Spanish (Andorra) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Andorra) per Firefox
Summary(es.UTF-8):	Recursos españoles (Andorra) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Andory)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es_AR
Spanish (Spain) resources for Firefox.

%description -n mozilla-firefox-lang-es_AR -l ca.UTF-8
Recursos espanyols (Andorra) per Firefox.

%description -n mozilla-firefox-lang-es_AR -l es.UTF-8
Recursos españoles (Andorra) para Firefox.

%description -n mozilla-firefox-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Andory).

%package -n mozilla-firefox-lang-es_CL
Summary:	Spanish (Chile) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Xile) per Firefox
Summary(es.UTF-8):	Recursos españoles (Chile) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Chile)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es_CL
Spanish (Chile) resources for Firefox.

%description -n mozilla-firefox-lang-es_CL -l ca.UTF-8
Recursos espanyols (Xile) per Firefox.

%description -n mozilla-firefox-lang-es_CL -l es.UTF-8
Recursos españoles (Chile) para Firefox.

%description -n mozilla-firefox-lang-es_CL -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Chile).

%package -n mozilla-firefox-lang-es
Summary:	Spanish (Spain) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Espanya) per Firefox
Summary(es.UTF-8):	Recursos españoles (España) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Hiszpanii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es
Spanish (Spain) resources for Firefox.

%description -n mozilla-firefox-lang-es -l ca.UTF-8
Recursos espanyols (Espanya) per Firefox.

%description -n mozilla-firefox-lang-es -l es.UTF-8
Recursos españoles (España) para Firefox.

%description -n mozilla-firefox-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Hiszpanii).

%package -n mozilla-firefox-lang-es_MX
Summary:	Spanish (Mexico) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Mèxic) per Firefox
Summary(es.UTF-8):	Recursos españoles (México) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Meksyku)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es_MX
Spanish (Mexico) resources for Firefox.

%description -n mozilla-firefox-lang-es_MX -l ca.UTF-8
Recursos espanyols (Mèxic) per Firefox.

%description -n mozilla-firefox-lang-es_MX -l es.UTF-8
Recursos españoles (México) para Firefox.

%description -n mozilla-firefox-lang-es_MX -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Meksyku).

%package -n mozilla-firefox-lang-et
Summary:	Estonian resources for Firefox
Summary(pl.UTF-8):	Estońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-et
Estonian resources for Firefox.

%description -n mozilla-firefox-lang-et -l pl.UTF-8
Estońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-eu
Summary:	Basque resources for Firefox
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-eu
Basque resources for Firefox.

%description -n mozilla-firefox-lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-fa
Summary:	Persian resources for Firefox
Summary(pl.UTF-8):	Perskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fa
Persian resources for Firefox.

%description -n mozilla-firefox-lang-fa -l pl.UTF-8
Perskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ff
Summary:	Fulah resources for Firefox
Summary(pl.UTF-8):	Pliki językowe fulani dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ff
Fulah resources for Firefox.

%description -n mozilla-firefox-lang-ff -l pl.UTF-8
Pliki językowe fulani dla Firefoksa.

%package -n mozilla-firefox-lang-fi
Summary:	Finnish resources for Firefox
Summary(pl.UTF-8):	Fińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fi
Finnish resources for Firefox.

%description -n mozilla-firefox-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-fr
Summary:	French resources for Firefox
Summary(pl.UTF-8):	Francuskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fr
French resources for Firefox.

%description -n mozilla-firefox-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-fy
Summary:	Frisian resources for Firefox
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fy
Frisian resources for Firefox.

%description -n mozilla-firefox-lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ga
Summary:	Irish resources for Firefox
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ga
Irish resources for Firefox.

%description -n mozilla-firefox-lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-gd
Summary:	Gaelic resources for Firefox
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-gd
Gaelic resources for Firefox.

%description -n mozilla-firefox-lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-gl
Summary:	Galician resources for Firefox
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-gl
Galician resources for Firefox.

%description -n mozilla-firefox-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-gu
Summary:	Gujarati resources for Firefox
Summary(pl.UTF-8):	Pliki językowe gudźarati dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-gu
Gujarati resources for Firefox.

%description -n mozilla-firefox-lang-gu -l pl.UTF-8
Pliki językowe gudźarati dla Firefoksa.

%package -n mozilla-firefox-lang-he
Summary:	Hebrew resources for Firefox
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-he
Hebrew resources for Firefox.

%description -n mozilla-firefox-lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hi
Summary:	Hindi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe hindi dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hi
Hindi resources for Firefox.

%description -n mozilla-firefox-lang-hi -l pl.UTF-8
Pliki językowe hindi dla Firefoksa.

%package -n mozilla-firefox-lang-hr
Summary:	Croatian resources for Firefox
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hr
Croatian resources for Firefox.

%description -n mozilla-firefox-lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hsb
Summary:	Upper Sorbian resources for Firefox
Summary(pl.UTF-8):	Górnołużyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hsb
Upper Sorbian resources for Firefox.

%description -n mozilla-firefox-lang-hsb -l pl.UTF-8
Górnołużyckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hu
Summary:	Hungarian resources for Firefox
Summary(hu.UTF-8):	Magyar nyelv Firefox-hez
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hu
Hungarian resources for Firefox.

%description -n mozilla-firefox-lang-hu -l hu.UTF-8
Magyar nyelv Firefox-hez.

%description -n mozilla-firefox-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hy
Summary:	Armenian resources for Firefox
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hy
Armenian resources for Firefox.

%description -n mozilla-firefox-lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-id
Summary:	Indonesian resources for Firefox
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-id
Indonesian resources for Firefox.

%description -n mozilla-firefox-lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-is
Summary:	Icelandic resources for Firefox
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-is
Icelandic resources for Firefox.

%description -n mozilla-firefox-lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-it
Summary:	Italian resources for Firefox
Summary(pl.UTF-8):	Włoskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-it
Italian resources for Firefox.

%description -n mozilla-firefox-lang-it -l pl.UTF-8
Włoskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ja
Summary:	Japanese resources for Firefox
Summary(pl.UTF-8):	Japońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ja
Japanese resources for Firefox.

%description -n mozilla-firefox-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-kk
Summary:	Kazakh resources for Firefox
Summary(pl.UTF-8):	Kazachskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-kk
Kazakh resources for Firefox.

%description -n mozilla-firefox-lang-kk -l pl.UTF-8
Kazachskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-km
Summary:	Khmer resources for Firefox
Summary(pl.UTF-8):	Khmerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-km
Khmer resources for Firefox.

%description -n mozilla-firefox-lang-km -l pl.UTF-8
Khmerskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-kn
Summary:	Kannada resources for Firefox
Summary(pl.UTF-8):	Pliki językowe kannada dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-kn
Kannada resources for Firefox.

%description -n mozilla-firefox-lang-kn -l pl.UTF-8
Pliki językowe kannada dla Firefoksa.

%package -n mozilla-firefox-lang-ko
Summary:	Korean resources for Firefox
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ko
Korean resources for Firefox.

%description -n mozilla-firefox-lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ku
Summary:	Kurdish resources for Firefox
Summary(pl.UTF-8):	Kurdyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ku
Kurdish resources for Firefox.

%description -n mozilla-firefox-lang-ku -l pl.UTF-8
Kurdyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-lij
Summary:	Ligurian resources for Firefox
Summary(pl.UTF-8):	Liguryjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-lij
Ligurian resources for Firefox.

%description -n mozilla-firefox-lang-lij -l pl.UTF-8
Liguryjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-lt
Summary:	Lithuanian resources for Firefox
Summary(pl.UTF-8):	Litewskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-lt
Lithuanian resources for Firefox.

%description -n mozilla-firefox-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-lv
Summary:	Latvian resources for Firefox
Summary(pl.UTF-8):	Łotewskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-lv
Latvian resources for Firefox.

%description -n mozilla-firefox-lang-lv -l pl.UTF-8
Łotewskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-mai
Summary:	Maithili resources for Firefox
Summary(pl.UTF-8):	Pliki językowe maithili dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-mai
Maithili resources for Firefox.

%description -n mozilla-firefox-lang-mai -l pl.UTF-8
Pliki językowe maithili dla Firefoksa.

%package -n mozilla-firefox-lang-mk
Summary:	Macedonian resources for Firefox
Summary(pl.UTF-8):	Macedońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-mk
Macedonian resources for Firefox.

%description -n mozilla-firefox-lang-mk -l pl.UTF-8
Macedońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ml
Summary:	Malayalam resources for Firefox
Summary(pl.UTF-8):	Pliki językowe malajalam dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ml
Malayalam resources for Firefox.

%description -n mozilla-firefox-lang-ml -l pl.UTF-8
Pliki językowe malajalam dla Firefoksa.

%package -n mozilla-firefox-lang-mr
Summary:	Marathi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe marathi dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-mr
Marathi resources for Firefox.

%description -n mozilla-firefox-lang-mr -l pl.UTF-8
Pliki językowe marathi dla Firefoksa.

%package -n mozilla-firefox-lang-ms
Summary:	Malay resources for Firefox
Summary(pl.UTF-8):	Malajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ms
Malay resources for Firefox.

%description -n mozilla-firefox-lang-ms -l pl.UTF-8
Malajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-nb
Summary:	Norwegian Bokmaal resources for Firefox
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-nb
Norwegian Bokmaal resources for Firefox.

%description -n mozilla-firefox-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-nl
Summary:	Dutch resources for Firefox
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-nl
Dutch resources for Firefox.

%description -n mozilla-firefox-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-nn
Summary:	Norwegian Nynorsk resources for Firefox
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-nn
Norwegian Nynorsk resources for Firefox.

%description -n mozilla-firefox-lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-or
Summary:	Oriya resources for Firefox
Summary(pl.UTF-8):	Pliki językowe orija dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-or
Oriya resources for Firefox.

%description -n mozilla-firefox-lang-or -l pl.UTF-8
Pliki językowe orija dla Firefoksa.

%package -n mozilla-firefox-lang-pa
Summary:	Panjabi resources for Firefox
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pa
Panjabi resources for Firefox.

%description -n mozilla-firefox-lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-pl
Summary:	Polish resources for Firefox
Summary(pl.UTF-8):	Polskie pliki językowe dla Firefoksa
Group:		I18n
URL:		http://www.firefox.pl/
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pl
Polish resources for Firefox.

%description -n mozilla-firefox-lang-pl -l pl.UTF-8
Polskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-pt_BR
Summary:	Portuguese (Brazil) resources for Firefox
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pt_BR
Portuguese (Brazil) resources for Firefox.

%description -n mozilla-firefox-lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-pt
Summary:	Portuguese (Portugal) resources for Firefox
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Firefoksa (wersja dla Portugalii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pt
Portuguese (Portugal) resources for Firefox.

%description -n mozilla-firefox-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Firefoksa (wersja dla Portugalii).

%package -n mozilla-firefox-lang-rm
Summary:	Romansh resources for Firefox
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-rm
Romansh resources for Firefox.

%description -n mozilla-firefox-lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ro
Summary:	Romanian resources for Firefox
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ro
Romanian resources for Firefox.

%description -n mozilla-firefox-lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ru
Summary:	Russian resources for Firefox
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ru
Russian resources for Firefox.

%description -n mozilla-firefox-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-si
Summary:	Sinhala resources for Firefox
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-si
Sinhala resources for Firefox.

%description -n mozilla-firefox-lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sk
Summary:	Slovak resources for Firefox
Summary(pl.UTF-8):	Słowackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sk
Slovak resources for Firefox.

%description -n mozilla-firefox-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sl
Summary:	Slovene resources for Firefox
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sl
Slovene resources for Firefox.

%description -n mozilla-firefox-lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-son
Summary:	Songhai resources for Firefox
Summary(pl.UTF-8):	Songhajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-son
Songhai resources for Firefox.

%description -n mozilla-firefox-lang-son -l pl.UTF-8
Songhajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sq
Summary:	Albanian resources for Firefox
Summary(pl.UTF-8):	Albańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sq
Albanian resources for Firefox.

%description -n mozilla-firefox-lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sr
Summary:	Serbian resources for Firefox
Summary(pl.UTF-8):	Serbskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sr
Serbian resources for Firefox.

%description -n mozilla-firefox-lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sv
Summary:	Swedish resources for Firefox
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sv
Swedish resources for Firefox.

%description -n mozilla-firefox-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ta
Summary:	Tamil (India) resources for Firefox
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ta
Tamil (India) resources for Firefox.

%description -n mozilla-firefox-lang-ta -l pl.UTF-8
Tamilskie pliki językowe dla Firefoksa (wersja dla Indii).

%package -n mozilla-firefox-lang-te
Summary:	Telugu resources for Firefox
Summary(pl.UTF-8):	Pliki językowe telugu dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-te
Telugu resources for Firefox.

%description -n mozilla-firefox-lang-te -l pl.UTF-8
Pliki językowe telugu dla Firefoksa.

%package -n mozilla-firefox-lang-th
Summary:	Thai resources for Firefox
Summary(pl.UTF-8):	Tajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-th
Thai resources for Firefox.

%description -n mozilla-firefox-lang-th -l pl.UTF-8
Tajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-tr
Summary:	Turkish resources for Firefox
Summary(pl.UTF-8):	Tureckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-tr
Turkish resources for Firefox.

%description -n mozilla-firefox-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-uk
Summary:	Ukrainian resources for Firefox
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-uk
Ukrainian resources for Firefox.

%description -n mozilla-firefox-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-vi
Summary:	Vietmanese resources for Firefox
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-vi
Vietmanese resources for Firefox.

%description -n mozilla-firefox-lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-xh
Summary:	Xhosa resources for Firefox
Summary(pl.UTF-8):	Pliki językowe xhosa dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-xh
Xhosa resources for Firefox.

%description -n mozilla-firefox-lang-xh -l pl.UTF-8
Pliki językowe xhosa dla Firefoksa.

%package -n mozilla-firefox-lang-zh_CN
Summary:	Simplified Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-zh_CN
Simplified Chinese resources for Firefox.

%description -n mozilla-firefox-lang-zh_CN -l pl.UTF-8
Chińskie uproszczone pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-zh_TW
Summary:	Traditional Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-zh_TW
Traditional Chinese resources for Firefox.

%description -n mozilla-firefox-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-zu
Summary:	Zulu resources for Firefox
Summary(pl.UTF-8):	Zuluskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-zu
Zulu resources for Firefox.

%description -n mozilla-firefox-lang-zu -l pl.UTF-8
Zuluskie pliki językowe dla Firefoksa.

%prep
unpack() {
    local args="$1" file="$2"
	local lang=$(basename $file .xpi)
	install -d $lang
	cd $lang
	cp -p $file .
	cd ..
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 90 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{firefoxdir}/extensions
for a in */*.xpi; do
	basename=$(basename $a .xpi)
	cp -p $a $RPM_BUILD_ROOT%{firefoxdir}/extensions/langpack-$basename@firefox.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n mozilla-firefox-lang-ach
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ach@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-af
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-af@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-an
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-an@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ar
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ar@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-as
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-as@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ast
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ast@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-az
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-az@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-be
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-be@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bg
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bg@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bn
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bn-BD@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bn_IN
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bn-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-br
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-br@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bs
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bs@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ca
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ca@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-cs
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-cs@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-csb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-csb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-cy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-cy@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-da
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-da@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-de
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-de@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-dsb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-dsb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-el
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-el@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-en_GB
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-en-GB@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-en_US
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-en-US@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-en_ZA
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-en-ZA@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-eo
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-eo@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es_AR
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-AR@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es_CL
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-CL@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-ES@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es_MX
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-MX@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-et
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-et@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-eu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-eu@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fa
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fa@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ff
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ff@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fi
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fi@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fy-NL@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ga
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ga-IE@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-gd
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-gd@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-gl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-gl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-gu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-gu-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-he
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-he@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hi
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hi-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hsb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hsb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hu@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hy-AM@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-id
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-id@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-is
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-is@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-it
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-it@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ja
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ja@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-kk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-kk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-km
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-km@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-kn
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-kn@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ko
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ko@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ku
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ku@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-lij
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-lij@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-lt
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-lt@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-lv
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-lv@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-mai
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-mai@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-mk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-mk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ml
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ml@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-mr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-mr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ms
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ms@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-nb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-nb-NO@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-nl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-nl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-nn
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-nn-NO@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-or
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-or@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pa
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pa-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pt_BR
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pt-BR@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pt
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pt-PT@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-rm
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-rm@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ro
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ro@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ru
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ru@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-si
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-si@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-son
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-son@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sq
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sq@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sv
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sv-SE@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ta
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ta@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-te
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-te@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-th
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-th@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-tr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-tr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-uk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-uk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-vi
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-vi@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-xh
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-xh@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-zh_CN
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-zh-CN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-zh_TW
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-zh-TW@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-zu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-zu@firefox.mozilla.org.xpi
