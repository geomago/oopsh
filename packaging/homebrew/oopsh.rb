class Oopsh < Formula
  include Language::Python::Virtualenv

  desc "Corrects your previous console command (maintained fork of thefuck)"
  homepage "https://github.com/geomago/oopsh"
  url "https://files.pythonhosted.org/packages/43/3d/216d210ee5d05cc578c55df08c03f45041fdc5c49c8b019cd83a7772a46e/oopsh-1.1.2.tar.gz"
  sha256 "430891a02af7717cf961c3dadf599de274635a78d6b522904745413eeaaf2a91"
  license "MIT"

  depends_on "python@3.14"

  resource "colorama" do
    url "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz"
    sha256 "08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"
  end

  resource "decorator" do
    url "https://files.pythonhosted.org/packages/60/8b/32f9823da46cde7df2087faa08cd98d01b908f8dcab982cdba9c84e85355/decorator-5.3.1.tar.gz"
    sha256 "4cbcdd55a6efadb9dbea26b858f4fb3264567b52d69ca0d25b721b553f60ea82"
  end

  resource "psutil" do
    url "https://files.pythonhosted.org/packages/aa/c6/d1ddf4abb55e93cebc4f2ed8b5d6dbad109ecb8d63748dd2b20ab5e57ebe/psutil-7.2.2.tar.gz"
    sha256 "0746f5f8d406af344fd547f1c8daa5f5c33dbc293bb8d6a16d80b4bb88f59372"
  end

  resource "pyte" do
    url "https://files.pythonhosted.org/packages/ab/ab/b599762933eba04de7dc5b31ae083112a6c9a9db15b01d3109ad797559d9/pyte-0.8.2.tar.gz"
    sha256 "5af970e843fa96a97149d64e170c984721f20e52227a2f57f0a54207f08f083f"
  end

  resource "wcwidth" do
    url "https://files.pythonhosted.org/packages/f0/b4/7830542634bb2d3e62aa3b586a72d5b3b6c91c3168929e7000ef3fed041d/wcwidth-0.9.2.tar.gz"
    sha256 "ae0ef90b90f6af38b54f1fe6d58662ec33b3cb4b8391958a62416d654231727b"
  end

  def install
    virtualenv_install_with_resources
  end

  def caveats
    <<~EOS
      Add this line to your ~/.zshrc or ~/.bashrc, then open a new shell:
        eval "$(oopsh --alias)"
      Then type `oops` after a mistyped command.
    EOS
  end

  test do
    assert_match "oopsh #{version}", shell_output("#{bin}/oopsh --version 2>&1")
    assert_match "oops ()", shell_output("TF_SHELL=zsh #{bin}/oopsh --alias")
  end
end
