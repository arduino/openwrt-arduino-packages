#
# Copyright (C) 2008 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=avrdude-yun
PKG_VERSION:=6.3
PKG_RELEASE:=3

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=git://github.com/facchinm/avrdude.git
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_SOURCE_VERSION:=1e0284ded3ce4fce881d12678b403cd747e2a7e0
PKG_SOURCE_SUBDIR:=$(PKG_NAME)
PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)

include $(INCLUDE_DIR)/package.mk

define Package/avrdude-yun
  SECTION:=utils
  CATEGORY:=Utilities
  TITLE:=AVR Downloader/UploaDEr (Yun version)
  URL:=http://www.bsdhome.com/avrdude/
  DEPENDS:=+libncurses +libreadline +libusb-compat +libftdi +libelf1 +libftdi1 +hidapi
endef

define Package/avrdude-yun/description
 AVRDUDE is a full featured program for programming Atmel's AVR CPU's.
endef

define Build/Prepare
	$(call Build/Prepare/Default)
	chmod -R u+w $(PKG_BUILD_DIR)
endef

define Package/avrdude-yun/conffiles
/etc/avrdude.conf
endef

CONFIGURE_ARGS+= \
	--disable-doc \
	--disable-parport \
	--enable-linuxgpio \

PKG_SOURCE_DIR:=$(PKG_NAME)
CONFIGURE_VARS += \
	ac_cv_lib_elf_elf_begin=no \

define Build/Configure 
	( cd $(PKG_BUILD_DIR); ./bootstrap )
	$(call Build/Configure/Default)
endef

define Build/Compile
	$(MAKE) -C $(PKG_BUILD_DIR) \
		DESTDIR="$(PKG_INSTALL_DIR)" \
		install
endef

define Package/avrdude-yun/install
	$(INSTALL_DIR) $(1)/etc
	$(INSTALL_CONF) ./files/avrdude.conf $(1)/etc/
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/avrdude $(1)/usr/bin/
endef

$(eval $(call BuildPackage,avrdude-yun))
