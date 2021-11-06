; ModuleID = "example2.rad"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"() 
{
entry:
  %"adding" = add i32 10, 20
  %"adding.1" = add i32 %"adding", 15
  ret i32 %"adding.1"
}
