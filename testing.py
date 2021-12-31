'''
SOFTWARE TESTING:
-->      types
-->      how to do
-->      advantages and disadvantages

A software testing is a process to identify the correctness,completeness and quality of computer software developed.
It includes a set of activities conducted with intent of finding errors in developed software so it will be corrected before  product
gets released to end users.

STAGES of Software Development  :  * requirement analysis
                                   * design
                                   * Development(implementation)
                                   * Testing
                                   * maintenance

TYPES OF SOFTWARE TESTING :  --> Manual testing
                             --> Automated testing
-----------------------------------------------------------------------------------------------------------------------------------------


1. MANUAL TESTING:
                 It is the process where testing of a web application which is done manually by human action to find defects and
                 bugs.Test cases are executed manually by human without support of tools or scripts.

 ADVANTAGES:

 1. LIVE TESTING :   Testers can test the application under similar conditions, any glitches or errors which occur can be tracked
                     easily.We can call it as 'LIVE TESTING'

 2. LESS PROGRAMMING KNOWLEDGE:  The main focus is on requirements, documenting test cases and executing them,so focus on programming
                                 is usually less that of automated test which is quite literally robotic,they fail to act as real end user
                                 world.

 3. UI and UX ISSUES : Manual testing helps tester to identify any related to the look and feel of application.It helps to find usability
                       issues in the application i.e any bugs and defects that may pop up as soon as user handles certain software in a way are
                       more likely to be solved.

 4. LOW INVESTMENT : Manual testing requires less investment and it doesn't require any costly tools or high level skills to perform
                     .It is cost effective short time scenarios

 5. ADAPTABILITY TO CHANGE : We can swiftly test and see the outcomes, so it is well suited in case when we are making a lot of
                             unplanned changes to our software applications and it should be tested immediately after implementing the
                             changes

--------------------------------------------------------------------------------------------------------------------------------
 -->  WHEN TO APPLY MANUAL TESTING?

     When the project is in initial development stage when the testing user interface especially with visual aspects as well
     if there is short term project mainly and the writing scripts will be time consuming in such cases we go for this testing than
     automated testing.
     These are main scenarios where manual testing is perferable over automated testing

 * EXPLORATORY TESTING : It is carried out by domain experts.It required testers knowledge and experience ,analytical and logical
                         skills creativity and intution.The test is carried out by poorly written documentation or a short time of
                         execution where we need human skills to execute the testing process.It requires minimal planning and maximum
                         test execution

 * USABILITY TESTING : It helps to find out the user friendliness of an application. In this area of value we need to measure
                       how user friendly, efficient and convenient the software is to end users. Human observation is important factor
                       along with experience and it requires no tools to perform test.

 * AD-HOC TESTING:   This testing doesnt follow any fixed method or approach so it is known as 'INFORMAL TESTING'.In this tester randomly
                     test the application without following any documents or any test design technique so understanding and insight are
                     mandatory

-------------------------------------------------------------------------------------------------------------------------------------------

  HOW TO PERFORM MANUAL TESTING?

  1. UNDERSTANDING THE REQUIREMENTS : By this we know what need to be tested and what classifies as defect or bug

  2. WRITING TEST CASES  :   It is another crucial part of manual testing once you understand requirements. These test cases guide
                             you through a sequence of tests to test functions and different scenarios written within software
                             application.writing good test cases are important as they make executing the test go very smoothly
                             also ensure good test coverage.

  3. TEST CONDUCTION :   Once test cases are written and test environment is prepared then test conduction comes to scenario.
                         we follow the test cases and mark each test as pass/failed or skipped.Keeping notes is mandatory when a
                         test fails and it is crucial shouldn't be ignored.

  4. LOG GOOD BUG REPORTS:  As we encounter bugs we need to inform log information for the development team about the defect.
                            A good bug report must have strong title, steps how to overcome the bug, expected and actual results
                            and any relevant attachments which help development team to understand the bug issue like screen shots
                            or recordings or export files.

  5. REPORT THE RESULTS : How many tests were run, how many were failed ,how many are left

---------------------------------------------------------------------------------------------------------------------------------

  DIFFERENT TYPES OF MANUAL TESTING:

  --> Basically divided into 6 types but these are carried out either manually or by automation

  1. BLACK BOX TESTING:
                      In this tester doesnt have any knowledge about the code or structure of software application which is tested
                      .He interacts with the application and test the functionality and nonfunctional behaviour of app.Various balck
                      box techniques used by tester to detect bugs/defects.

  2. WHITE BOX TESTING:
                     The tester knows about code and structure of application. It is also known as 'GLASS BOX OR TRANSPERANT BOX TESTING'
                     .It is used by developers mostly to perform unit testing.
                     Various white box testing can be used to find bugs/defects like CONTROL FLOW TESTING,DATA FLOW TESTING,BRANCH TESTING,
                     STATE TESTING ,DECISION COVERAGE, PATH TESTING

    (GREY BOX TESTING) : It is partial black box and partial white box ,we have info only about certain factors of an app

  3. UNIT TESTING:
                 This is 1st level of testing,it is the way of testing the smallest piece of code which referred as unit.This
                 unit can be logically isolated in a system.It mainly focussed on functional correctness of the standalone module it can be
                 specific piece of functionality /part of a code/program/particular method within the app it can be anything a unit. So this testing
                 uses white box testing methods/techniques and usually perform using preferrd programming language.
                 The developers need to unit test the software before handing it to QA team

                 ADVANTAGES:  It makes our code reusable as you need to use modular approach
                              It makes debugging lot easier so it is performed before moving to next stage of testing

  4. INTEGRATION TESTING:
                    It is performed after unit testing where different modules,components,units of software or application in testing
                    are integrated together. Its motto is to verify functionality, stability and reliability of modules when combined
                    together. The main focus is to check the correctness of communication among all these modules/units.

  5. SYSTEM TESTING:
                   It is the next step after integration testing, it is carried out complete fully integrated software developed
                   to evaluate the behaviour of the system in our entire fashion & then to examine how the full working of integrated software
                   computer system against given requirements, the entire application as whole is tested here.
                   So many system testing techinques like functionality testing, performance scalability,stress testing and regression testing

  6. USER ACCEPTANCE TESTING:
                   This formal testing is performed based on user requirements and function processing. this type covers end user
                   real world scenarios.It is the last which needs to be done correctly because it will provide final results on this basis our software
                   either approved or rejected

------------------------------------------------------------------------------------------------------------------------------
 DISADVANTAGES OF MANUAL TESTING:

 * Time consuming  : if there is a change in application the tester need to do all test cases again from beginning
                     tester should test the app even if it is minor change

 * Possibility of errors : Manual testing is dependent on humans and chances to get errors because testing results are based on
                           testers performance

 * Testing limitations : Manual testing is not good for load and performance testing, to check the performance of an app there is large
                         requirement of users and gadgets

-------------------------------------------------------------------------------------------------------------------------------
MANUAL TESTING                                                                              AUTOMATED TESTING

1. GUARANTEE USER FRIENDLINESS                                                               DOESN'T GUARANTEE
2. VERY TIME CONSUMING                                                                       SIGNIFICANTLY FASTER
3. NOT ACCURATE EVERY TIME                                                                   HIGH ACCURACY
4. CAN'T BE ACCLIAMED AS RELIABLE                                                            COMPARITIVELY MORE RELIABLE
5. NEEDS NO PROGRAMMING EFFORTS                                                               PROGRAMMING REQUIRED
6. NOT MUCH EXPENSIVE                                                                         EXPENSIVE
7.INVESTMENT IN TERMS OF HUMAN RESOURCES                                                      IN TERMS OF PURCHASING TOOLS





















'''