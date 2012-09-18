/* 
Copyright 2012 Hardcoded Software (http://www.hardcoded.net)

This software is licensed under the "BSD" License as described in the "LICENSE" file, 
which should be included with this package. The terms are also available at 
http://www.hardcoded.net/licenses/bsd_license
*/

#import <Cocoa/Cocoa.h>
#import "HSGUIController.h"
#import "MGChartView.h"
#import "PyChart.h"

@interface MGChart : HSGUIController {}
- (id)initWithPyRef:(PyObject *)aPyRef;
- (MGChartView *)view;
- (PyChart *)model;

- (NSDictionary *)fontAttributesForID:(NSInteger)aFontID;

/* Python callbacks */
- (void)refresh;
- (void)drawText:(NSString *)aText inRect:(NSRect)aRect withFontID:(NSInteger)aFontID;
- (NSSize)sizeForText:(NSString *)aText withFontID:(NSInteger)aFontID;
@end
