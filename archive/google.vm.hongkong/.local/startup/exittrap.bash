# XROOT
#
# Utility functions to controll exiting of bash shells.
#
# Problem:
#    Exitting a bash shell is done by the 'exit' command. Unfortunately, exitting
#    from the root bash shell of a bash session will close the session. This makes
#    the 'exit' command somewhat dangerous, especially when frequently creating and
#    exitting from subshells. By exitting at the wrong time, a session may be killed.
#
# Puropose:
#    To provide a replacement for the builtin 'exit' command which will behave 
#    identically to the builtin 'exit' command, except that it will not exit from
#    the root shell. By using the replacement command, the above problem is solved.
#
# Use:
#    Have this script sourced by [~/.bashrc] and, if needed, by [~/.profile], and
#    restart bash. The following commands will be available:
#        leave   -- wrapper for the exit command
#        safe    -- a command which tells whether it is safe to exit.
#
# Implementation:
#    Assume we (ie this script) is sourced at the start of every session shell.
#    When we are first sourced, we should find the environment variable "${XROOT}"
#    unset. Finding it unset, we set it to our current PID (processes id), given
#    by the special variable "$$". Thereafter, one can tell whether or not we are
#    one is in the root shell by comparing one's current PID "$$" to the PID stored
#    in ${XROOT}.
#


#=====================================================================================
# ENVIRONMENT VARIABLES
#=====================================================================================


#------------------------------------------------------------------------------------
# If this is the first time this script is sourced (normally at the startup of the
# root bash shell) then ${XROOT} is not yet set. In that case we set it to the PID
# of the current shell. Otherwise we are in a subshell and leave ${XROOT} unchanged.

[ "$XROOT" = "" ] && echo SETTING XROOT TO $$
[ "$XROOT" = "" ] && export XROOT=$$
[ "$XROOT" = "" ] && export XROOT=$$


#=====================================================================================
# FUNCTIONS
#=====================================================================================

safe () { 
    # Compare XROOT to $$ and report whether it is safe to exit
    [ "$XROOT" == "$$" ] && echo not safe to exit
    [ "$XROOT" == "$$" ] || echo safe to exit
}

exit () {
    # Compare XROOT to $$ and exit only if safe. Othgerwise report.
    [ "$XROOT" == "$$" ] && echo -e "you cannot exit the root shell (pid ${XROOT}).\ntry \"builtin exit\""
    [ "$XROOT" == "$$" ] || { echo exitting shell pid $$ ; builtin exit  2> /dev/null; }
}

