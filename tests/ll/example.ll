; ModuleID = "example.rad"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"() 
{
entry:
  %"adding" = add i32 10, 20
  ret i32 %"adding"
}
