import subprocess
import os

def execute_command(command):
    try:
        # Splitting command by space to get arguments
        args = command.split()
        
        # Checking for IO redirection
        input_file = None
        output_file = None
        
        if '<' in args:
            input_index = args.index('<')
            input_file = args[input_index + 1]
            args = args[:input_index]
        
        if '>' in args:
            output_index = args.index('>')
            output_file = args[output_index + 1]
            args = args[:output_index]
        
        # Executing the command
        if '|' in args:
            # Handling piping
            command1, command2 = ' '.join(args[:args.index('|')]), ' '.join(args[args.index('|')+1:])
            proc1 = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE)
            proc2 = subprocess.Popen(command2, shell=True, stdin=proc1.stdout)
            proc1.stdout.close()  # Allow proc1 to receive a SIGPIPE if proc2 exits.
            return proc2.communicate()[0].decode()
        else:
            # Normal command execution
            process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            
            if output_file:
                with open(output_file, 'wb') as f:
                    f.write(output)
            else:
                print(output.decode())
                
            if error:
                print(error.decode())
            
            if input_file:
                os.remove(input_file)  # Remove input file after processing
        
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        command = input("Enter command (or 'exit' to quit): ")
        if command.lower() == 'exit':
            break
        execute_command(command)

if __name__ == "__main__":
    main()
