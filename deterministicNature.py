#DETERMINISTIC NATURE OF COMPUTING
****In computer science, when we say a system is deterministic, we mean thet the same input
and the same instructions will always priduce the same output. A computer cannot decide
to do something different because it feels like it.
****A computer is not smart in the way a person is smart. it is extremely fast at doing 
very simple things, but it has no understanding of the real world. if you give it the wrong
instructions, it will produce the wrong result without complaining.

****Inside every computer, processor, phone, and ATM, there are billions of tiny operations 
happening. But each operation is simple. The computer can:(1) store a number,(2) Read a number
(3) Compare two numbers,(4) Add, subtract, multiply, or divide numbers. (5) move data from 
one place to another. (6) Decide between two paths based on a condition.

****The word "compute" means to calculate or process information. A computer's job is to process 
information using a serise of instructions. The instructions are called a program. The person who 
writes those instructions is a programmer. 

***Deterministic behavior is not a weakness.It is the reason we can trust computers with
serious tasks.
***Predictability is a feature. It means we can test software, find errors, and fix them.
If the same input always gives the same output, then we can observe what went wrong and
correct the instructions.
****Most of the time, the computer is behaving exactly as instructed.
The fault is in the instructions. This is why programmers say,
"It's not a bug in the computer; it's a bug in the code." A bug is a mistake in the program.

##ALGORITHMIC SEQUENCING
****In programming, an atomic operation is a step that we treat as one single action at the level we
are working. It may be made up of even smaller actions in the physical world, but for our algorithm,
we treat it as one clear unit.

###Sequential execution
****At the heart of algorithmic sequencing is sequential execution. This means steps are performed
one after another, in the order they are written. Each step completes before the next begins.
 ***Sequential execution is like following a numbered list to prepare a meal. Sequential execution
 is the default behavior of every computer program. Even when decisions and repetitions appear,
 the flow always moves through the sequence step by step.

##Decomposition into atomic operations
****Deconstruction means taking a large task and separating it into its parts. In programming, we
do this constantly. We start a goal thar sounds simple to a human, and we turn it into a list of
atomic operations. 

###Conditional Branching/decision points
****Not all tasks are straight lines. Sometimes the next step depends on a condition. This is where
conditional branching comes in.
A program can look at its current state, evaluate a condition, and then choose one of two or more
paths.
**The simplest form is an if/else branch:
IF the PIN is correct: proceed to the next step ELSE: show "Incorrect PIN".
The program does not continue blindly. It checks. If the condition is true, it follows one branch.
If the condition is false, it follows another. 
***Conditional branching is essential because the real world has many possible cases.
A program that only followed one fixed path would be useless. With branching, the same program 
can handle correct PINs, wrong PINs, sufficient funds, and insufficient funds.
**We can combine branching with sequence. A program may:
    *Perform a sequence of steps.
    *Hit a condition.
    *Branch.
    *Continue a sequence.
    *Hit another condition.
    *Branch again.
This creates a flow of logic that adapts to the situation while still being deterministic.
***Atomic operations are precise. The operations are the smaller actions that lead to a goal.

###SUMMARY 
****A complex goal must be broken down into smaller, atomic operations.
****Atomic operations are clear, simple, and unambiguous enough for a machine to follow.
****Sequential execution means steps run one after another in order.
****Conditional branching allows a program to take different paths based on conditions.
****Each step usually depends on the state produced by previous steps.
****Vague instructions create failure points because computers do not fill in gaps.
****Deconstruction is a fundamental skill for programmers.