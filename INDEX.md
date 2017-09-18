[C on Tutorialspoint](https://www.tutorialspoint.com/cprogramming/c_overview.htm) | [Document Source](./INDEX.md)

SOFE 3200 Tutorials: Part 1
===========================

## Intro. to Linux, its Utilities, and Review of C

&nbsp;

## Downloading This Tutorial

You can use the following `wget` command to download INDEX.md to your working directory.

```sh
wget http://ericdube.com/sofe3200/1/INDEX.md
```

In Ubuntu, enter `Ctrl+Alt+T`, then enter the above command in the terminal
window that appears.

## Covered in This Tutorial

- [What is Systems Programming?](#what-is-sys)
- [What is Linux?](#what-is-linux)
- [Basic Commands](#commands)
- [Intro. to Vi](#vi-intro)
- [C Quiz](#c-quiz)
- [C Challenges](#c-challenge)

# <a name="what-is-sys"></a>What is Systems Programming?
## Not User-Facing
System programs are typically "invisible" to the user. For example, in order your
web browser and media player to use your speakers simultaneously, the operating
system has a "sound server", which most users won't know is there.

These programs perform functions required by the system or other programs.

## Systems Programming Examples

- Android OS
- Sound/Graphics servers
- Drivers or other **kernel modules**
- Window Manager
  - Not "invisible", but serves a necessary system function
- Many common libraries (GTK, Qt, .NET, Cairo)

[next](#what-is-linux)

# <a name="what-is-linux"></a>What is Linux?

## What is Linux?
### A Kernel
Primarily, Linux is a kernel. The kernel is the low-level component of the
operating system that does all the heavy-lifting, such as managing processes
and communicating with critical hardware components.

Specifically, Linux is a Monolithic kernel. You may want to read on Monolithic
vs Microkernels as it's an interesting topic.

### An Operating System
Many organizations offer complete operating systems using the Linux kernel,
known as **distributions**. One such example is Ubuntu from Canonical.

### Naming Controversy
There's actually disagreement as to whether the OS we know as Linux should
be called *Linux* or *GNU/Linux*. This is known as the
[Linux Naming Controversy](https://en.wikipedia.org/wiki/GNU/Linux_naming_controversy).

[next](#commands)

# <a name="commands"></a>Using the Terminal

## Basic Commands
| Command | Description |
| -- | -- |
| cd &lt;path&gt; | Change working directory |
| ls [path] | Show contents of working directory |
| rm &lt;path&gt; | Remove file at &lt;path&gt; |
| mv &lt;src&gt; &lt;dest&gt; | Move/rename a file or folder |
| cp &lt;src&gt; &lt;dest&gt; | Copy a file or folder |
| top | Show processes, CPU and RAM usage |
| cat &lt;path&gt;... | Display contents of one or more files |
| grep [OPTION]... PATTERN [FILE] | Search for a pattern using regex |

## Pipes and Redirection

Pipes are used to redirect the output of a program to the input of another
program. For example, we can pipe the output of `ls` into `grep` to show
only files matching a particular pattern.

```sh
# This command will show only files ending in .txt
ls | grep "\.txt$"
```

Redirection allows you to output to a file, or receive input from a file.
For example, we can concatenate two files using `cat`.

```sh
cat file1.txt file2.txt > file3.txt
```

## Basic Regex

A regular expression defines a pattern that can be matched in some input text.
The pattern contains the literal characters in order which you'd like to match,
as well as additional symbols which hold special meanings.

| Symbol | Meaning |
| -- | -- |
| `.` | Matches any character once |
| `*` | Matches the previous character zero or more times. For example, `.*` will match any string, including nothing at all. |
| `?` | Matches any character one or more times. For example, `?*` will match any string with at least one character. |
| `^` | Matches the beginning of a string. For example, `^note_` will match any string beginning with `note_`. |
| `$` | Matches the end of a string. For example, `\.txt$` will match any string ending with `.txt` |

These characters are essential in writing useful regular expressions, but this is
not a comprehensive list. To match a literal character that has a special meaning,
you must precede a backslash. For example, `\.` will match a literal dot.

**Note:** Many utilities available on *nix systems use **basic** regular expressions,
while you may be used to extended regular expressions. The syntax is mostly
identical, but a common mistake is to use regular parentheses (`(` and `)`) for
grouping and escaped parentheses (`\(` and `\)`) for literal brackets. In basic
regular expressions, these are reversed.

Regular-Expressions.info has a good reference
for [POSIX Basic Regular Expressions](http://www.regular-expressions.info/posix.html).

[next](#vi-intro)

# <a name="vi-intro"></a>Intro. to Vi

## Basic Examples
| Example | Result |
| -- | -- |
| `i` | Enter insert mode, in which text can be entered normally. |
| `ESC` | Return to normal mode. |
| `h`, `j`, `k`, `l` | Navigate left, down, up, and right respectively. |
| `dd` | Cut the current line. |
| `yy` | Copy the current line. |
| `2dd` | Cut two lines starting from the current line going down. |
| `2dl` | Cut two characters to the right of the cursor position. |
| `p` | Paste last deletion. (i.e. from last `d` or `y` action) |
| `o`, `O` | Add line below, and add line above respectively. Also enter insert mode. |

## Activity
Manipulate this list using Vi. Just follow any instructions in the same order
which they appear.
- This is the first item
- Delete this line using `dd`
- This is the second item
- Press `O` here, type "This is the third item", and press ESC
- Press `p` here

## Other editors
### Nano (`nano`)
Nano is a simple commandline text editor. It's easier to use than Vi but has
fewer features.

### Gedit and others (`gedit`, `kate`, `leafpad`)
Gedit is the default text editor in GNOME, a popular desktop environment for
Linux systems. Other distributions may have Kate (KDE's editor),
Leafpad (LXDE's editor), or one of many others.

### Popular Editors in Linux
Many of today's popular code editors, such as Atom, Sublime Text, and VSCode,
are available for all Linux distributions.

[next](#c-quiz)

# <a name="c-quiz"></a>C Quiz (Q1)

## Find the Error
```c
#include <stdio.h>

int main(char *argv[], int argc)
{
    printf("Hello, World!\n");
}
```

[next](#c-quiz-2)

# <a name="c-quiz-2"></a>C Quiz (Q2)

## Find the Error
```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    for (i = 0; i < 10; i++)
    {
        printf("Number %n\n", i)
    }
}
```

[next](#c-quiz-3)

# <a name="c-quiz-3"></a>C Quiz (Q3)

## What is the Output?
```c
#include <stdio.h>

int main()
{
		int  end = 10;
		for (int i=0; i < end; i++)
		{
				for (int j=0; j < end; j++)
				{
						printf( (j<i) ? " " : "*" );
				}
				printf("\n");
		}
}
```

[next](#c-chal-1)

# <a name="c-chal-1"></a>C Challenges (C1)

## Challenge: What is the Output?
```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
		if (argc < 2)
		{
				printf("usage: ./a.out <SIZE>\n");
				return 1;
		}
		// Size should be an even number
		int end = atoi(argv[1]);
		if (end % 2 == 1)
		{
				end--;
		}
		// Generate output
		for (int i=0; i <= end/2; i++)
		{
				for (int j=end/2-1; j >= 0; j--)
				{
						if (j < i) {
							printf("*");
						} else {
							printf(" ");
						}
				}
				printf("*");
				for (int j=0; j < end/2; j++)
				{
						if (j < i) {
							printf("*");
						} else {
							printf(" ");
						}
				}
				printf("\n");
		}
}

```

[next](#c-chal-2)

# <a name="c-chal-2"></a>C Challenges (C2)

## Challenge: What is the Output?
```c
// Upcoming
```
