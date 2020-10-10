


# ----------------------------------------------------------------------------
# invoke command by arguments
# ----------------------------------------------------------------------------

# if [[ -n $1 ]] ; then
#
#     print('')
#     FUNC=$1
#     shift;
#
#     # todo prompt help if FUNC=='-h'|'--help' or FUNC==None
#
#     # ---------------------------------------------
#     # setup test python3 environment using arguments
#     # ---------------------------------------------
#
#     for i in "$@"
#     do
#     case ${i} in
#
#         -p=*|--pre=*)
#         PRE_FILE="${i#*=}"
#         shift 1 # past argument=value
#         _pre ${PRE_FILE};
#         ;;
#
#         ---*=*)
#         VAL="${i#*---}"
#         shift 1 # past argument=value
#         print("export $VAL";
#         export ${VAL};
#         ;;
#
#     esac;
#     done;
#
#     # --------------------
#     # invoke test function
#     # --------------------
#
#     # print("${FUNC} $@";
#     ${FUNC} $@;
#
# else
#     print("please provide command for the auxilium script, e.g. 'setup', 'run', 'deploy', 'cleanup'";
# fi;
