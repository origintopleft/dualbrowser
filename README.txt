+======================+=================================================+
| Important Legal Note | (tl;dr "Don't blame me if this melts your dog") |
+======================+=================================================+
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

=== Prerequisites ===
- Windows (a Linux version was never needed when I used this)
- Python 2.7
- py2exe (currently no 3.x version, you're stuck with 2.7, sorry)
- PyQt4
- and I think there was a win32 module for process listing, I didn't actually
  look yet

=== Compile Instructions ===
1) Open dualbrowser.py in a plain text editor, and point the strings to the
   respective locations on your computer. This wasn't originally planned for
   release so I never bothered to make a config option for it.
2) python ./setup.py, hit yes

=== Usage Instructions ===
1) Edit the Windows registry to point to dualbrowser.exe as the program
   associated with http. I had originally planned for a way to make it the
   default "browser" from within the program, but then I became a pure Firefox
   user before I implemented it.
2) Open the config utility (should be dualbrowser.exe, no arguments) and get a
   feel for it. Default settings should be fine for general use.


This program will open URLs in whichever browser is already open (or if
neither browser is open, will open one at random if a preference is not set in
the config utility).
