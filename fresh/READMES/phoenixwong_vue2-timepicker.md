# Vue2 Timepicker  

![GitHub version](https://img.shields.io/github/package-json/v/phoenixwong/vue2-timepicker?color=success&style=flat-square)
![npm version](https://img.shields.io/npm/v/vue2-timepicker?style=flat-square)
![GitHub release](https://img.shields.io/github/release/phoenixwong/vue2-timepicker?label=github&style=flat-square)
![npm downloads](https://img.shields.io/npm/dm/vue2-timepicker?style=flat-square)

---

💡 Dead repo recharged 🔋

---

A dropdown time picker (hour|minute|second) for **Vue 2.x**, with flexible time format support.

## Demo

You can see the **Vue2 Timepicker** in action in the [Demo Page](https://phoenixwong.github.io/vue2-timepicker/)

## Migration

Please check [MIGRATION.md](https://github.com/phoenixwong/vue2-timepicker/blob/master/MIGRATION.md) for basic guidelines if you are about to:

- Migrate from the Vue 1.x version **[vue-time-picker](https://github.com/phoenixwong/vue-timepicker)**
- Migrate from Bower to Yarn or NPM (Vue2 Timepicker `v0.1.x` -> `v0.2.0+`)


## Dependencies

[Vue.js](http://vuejs.org/)&nbsp;&nbsp;&nbsp;![npm peer dependency version](https://img.shields.io/npm/dependency-version/vue2-timepicker/peer/vue?style=flat-square)

## Installation

```bash
yarn add vue2-timepicker
```

```bash
npm install vue2-timepicker --save
```

> NOTE: We stop Bower support from `0.2.0+`, please check [MIGRATION.md](https://github.com/phoenixwong/vue2-timepicker/blob/master/MIGRATION.md#migrating-from-bower-to-yarn-or-npm) for migration guidelines.

## Get Started

### **Step 1:** Import VueTimepicker

#### **Option A:** Import component JS and CSS

```javascript
// Main JS (in UMD format)
import VueTimepicker from 'vue2-timepicker'

// CSS
import 'vue2-timepicker/dist/VueTimepicker.css'
```

#### **Option B:** Choose any bundle version base on your needs

**Javascript**

```javascript
// CommonJS
import VueTimepicker from 'vue2-timepicker/dist/VueTimepicker.common.js'
// UMD
import VueTimepicker from 'vue2-timepicker/dist/VueTimepicker.umd.js'
// UMD Minified
import VueTimepicker from 'vue2-timepicker/dist/VueTimepicker.umd.min.js'
```

**CSS**

```css
@import 'vue2-timepicker/dist/VueTimepicker.css';

/* Or, with node_module alias path like: */
@import '~vue2-timepicker/dist/VueTimepicker.css';

/*
  NOTE: the path alias to `node_modules` differs between bundlers.
  Please change the `~` to any alias that works with your environment.
 */
```

**Single File Component**

```javascript
// The *.vue file with CSS included
import VueTimepicker from 'vue2-timepicker/src/vue-timepicker.vue'
// NOTE: In some cases, it requires additional workarounds in the bundler's config
```

#### **SSR Usage**

```javascript
// Import the *.vue file (CSS included)
import VueTimepicker from 'vue2-timepicker/sfc'
// Note the `/sfc` suffix here
```

If your server-side renderer cannot recognize the `/sfc` alias, please try --

```javascript
// Manually point to the `/src` folder
import VueTimepicker from 'vue2-timepicker/src'
// Or, to the specific file name
import VueTimepicker from 'vue2-timepicker/src/vue-timepicker.vue'
```

### **Step 2**: Include VueTimepicker in your component

```javascript
var yourComponent = new Vue({
  components: { VueTimepicker },
  ...
})
```

### **Step 3**: Put `vue-timepicker` in your component's template

Then, you can introduce the `vue-timepicker` tag anywhere you like in your component's template

```html
<vue-timepicker></vue-timepicker>
```


## Basic Usage

### Base

```html
<!-- Default to 24-Hour format HH:mm -->
<vue-timepicker></vue-timepicker>
```

### Customized Time Format

```html
<!-- Show seconds picker -->
<vue-timepicker format="HH:mm:ss"></vue-timepicker>

<!-- 12-hour format, with AM/PM picker -->
<vue-timepicker format="hh:mm A"></vue-timepicker>

<!-- 12-hour format, with seconds picker and am/pm picker -->
<vue-timepicker format="hh:mm:ss a"></vue-timepicker>
```

VueTimepicker recognizes the following tokens in the format string

Section    | Token | Output
---------- | ----- | ---------------
**AM/PM**  | A     | AM PM
&nbsp;     | a     | am pm
**Hour**   | H     | 0 1 ... 22 23
&nbsp;     | HH    | 00 01 ... 22 23
&nbsp;     | h     | 1 2 ... 11 12
&nbsp;     | hh    | 01 02 ... 11 12
&nbsp;     | k     | 1 2 ... 23 24
&nbsp;     | kk    | 01 02 ... 23 24
**Minute** | m     | 0 1 ... 58 59
&nbsp;     | mm    | 00 01 ... 58 59
**Second** | s     | 0 1 ... 58 59
&nbsp;     | ss    | 00 01 ... 58 59

> If not set, the `format` string is default to "HH:mm"

### Customized Picker Interval

```html
<!-- Show minute picker's value in the form of 0, 5, 10, ... 55, 60 -->
<vue-timepicker :minute-interval="5"></vue-timepicker>

<!-- Show second picker's value in the form of 0, 10, 20, ... 50, 60 -->
<vue-timepicker :second-interval="10"></vue-timepicker>

<!-- Bind interval config with your own data variable -->
<vue-timepicker :minute-interval="yourMinuteInterval"></vue-timepicker>
```


## Data Binding

### Bind Value with `v-model`

From `v1.0.0+`, timepicker's `v-model` accepts value in both _Object_ (default) and _String_ format. The `v0.x` versions only support _Object_ form.

#### Set Initial Value

For example, if you want to set "10:05:00" ("HH:mm:ss" format) as the initial value of vue-timepicker:

```javascript
const yourComponent = new Vue({
  components: { VueTimepicker },
  data () {
    return {
      // Object form
      yourTimeValue: {
        HH: '10',
        mm: '05',
        ss: '00'
      },
      // String form
      yourStringTimeValue: '10:05:00',
      ...
    }
  },
  ...
})
```

Both forms lead to the same result.

```html
<!-- Object form -->
<vue-timepicker v-model="yourTimeValue" format="HH:mm:ss"></vue-timepicker>

<!-- String form -->
<vue-timepicker v-model="yourStringTimeValue" format="HH:mm:ss"></vue-timepicker>
```

#### Set Empty Initial Value

When the initial value is completely unknown:

```javascript
data () {
  return {
    // Will be rendered as Object form
    yourEmptyValue: {},
    emptyValueToo: undefined,
    emptyValueAsWell: null,

    // Will be taken into String form
    yourEmptyStringValue: ''
  }
}
```

#### Set Partially-Known Initial Value

For instance, if you want to set the initial hour value to **8 pm** and leave the rest slots empty:

```javascript
data () {
  return {
    // OBJECT FORM
    // Default 24-Hour
    timeValue: {
      HH: '20',
      mm: ''
    },
    // 12-Hour with seconds
    timeValueWithSec: {
      h: '8',
      mm: '',
      ss: '',
      A: 'PM'
    },

    // STRING FORM
    // Default 24-Hour + String value
    stringTimeValue: '20:mm',
    // 12-Hour with seconds + String value
    stringTimeValueWithSec: '8:mm:ss PM'
  }
}
```

```html
<!-- OBJECT FORM -->
<!-- Default 24-Hour -->
<vue-timepicker v-model="timeValue"></vue-timepicker>
<!-- 12-Hour with seconds -->
<vue-timepicker v-model="timeValueWithSec" format="h:mm:ss A"></vue-timepicker>

<!-- STRING FORM -->
<!-- Default 24-Hour + String value -->
<vue-timepicker v-model="stringTimeValue"></vue-timepicker>
<!-- 12-Hour with seconds + String value -->
<vue-timepicker v-model="stringTimeValueWithSec" format="h:mm:ss A"></vue-timepicker>
```

### Get Time Picker's Current Value

#### Get value from `v-model`

You can either read the binding `v-model` value anytime or add a handler to deal with the `input` event from vue-timepicker.

```html
<vue-timepicker v-model="yourTimeValue" format="HH:mm:ss" @input="inputHandler"></vue-timepicker>
```

```javascript
{
  data () {
    return {
      yourTimeValue: {
        HH: '10',
        mm: '05',
        ss: '00'
      },
      ...
    }
  },

  methods: {
    inputHandler (eventData) {
      console.log(eventData)
    }
  }
}

```

In this case, we set the initial value (_yourTimeValue_) to "10:05:00". Then, open the dropdown picker and pick a new time, like setting it to "14:30:15" for example.

```javascript
// In `inputHandler`:
// console.log outputs -> {HH: "14", mm: "30", ss: "15"}
```

### Read Data From `change` Event

```html
<!-- A: No argument -->
<vue-timepicker v-model="yourTimeValue" @change="changeHandler"></vue-timepicker>

<!-- B: Custom arguments -->
<vue-timepicker v-model="yourTimeValue" @change="otherChangeHandler($event, 'foo', 42)"></vue-timepicker>
```

```javascript
// A: No argument
changeHandler (eventData) {
  console.log(eventData)
  // -> {data: {HH:..., mm:... }, displayTime: "HH:mm"}
}

// B: Custom arguments
otherChangeHandler (eventData, yourArg1, yourArg2) {
  console.log(eventData)
  // -> {data: {HH:..., mm:... }, displayTime: "HH:mm"}
  console.log(yourArg1)
  // -> 'foo'
  console.log(yourArg2)
  // -> 42
}
```

Unlike `v-model` and `input` event, which only return the defined time tokens you provided in the binding variable, the `change` event delivers **all** supported formats.

In the example above, after the user set values to "14:30:15" in the picker, `change` event returns the following data:

```javascript
// `@change` event data
{
  data: {
    HH: "14",
    H: "14",
    hh: "14",
    a: "am",
    A: "AM",
    h: "14",
    kk: "14",
    k: "14",
    m: "30",
    mm: "30",
    s: "15",
    ss: "15"
  },
  // extra `displayTime` added since v0.2.2
  displayTime: "14:30:15"
}
```

Whereas the `v-model` / `input` only return the data with defined tokens

```javascript
// Previously defined variable (`yourTimeValue` in this case) as {HH:..., mm:..., ss:...}
// Hence, the `v-model` returns:
{
  HH: "14",
  mm: "30",
  ss: "15"
}
```

## Advance Usage

### Hide Clear Button

```html
<vue-timepicker hide-clear-button></vue-timepicker>
```

Enable to hide the "&times;" clear button on the right-hand side. Users can still pick new values from the dropdown, but they cannot erase any selected data.

### Disable Picker

```html
<vue-timepicker disabled></vue-timepicker>
```

Fully disable both dropdown picker and the "&times;" clear button in the UI, to prevent users from changing any values again.

### Close on Complete

Automatically close the dropdown when the user finishes selecting **all** of the required fields.

```html
<vue-timepicker close-on-complete></vue-timepicker>
```

### Auto-Scroll

```html
<vue-timepicker auto-scroll></vue-timepicker>
```

Auto-scroll to selected values on dropdown open. It works with both:

- Programmatically defined value. E.g., the initial value from `v-model`
- Values manually picked by the user.

### Define Hour Range

Sometimes you may want to limit hours picker to a specific range. The `hour-range` parameter is here to help.

```html
<!-- 24-Hour Format -->
<vue-timepicker :hour-range="[5, [8, 12], [14, 17], 19]"></vue-timepicker>
<!-- >> Equals to :hour-range="[5, 8, 9, 10, 11, 12, 14, 15, 16, 17, 19]" -->

<!-- 12-Hour Format -->
<vue-timepicker :hour-range="['7a', '9a', '11a', '1p', ['3p', '5p'], '7p']" format="hh:mm a">
<!-- >> Equals to :hour-range="['7a', '9a', '11a', '1p', '3p', '4p', '5p', '7p']" -->
```

### Set Minute and Second Range

Similar to `hour-range`, you can determine values in the minutes and seconds dropdown by using `minute-range` and `second-range`.

```html
<!-- Minute range -->
<vue-timepicker :minute-range="[0, 6, [10, 30], 42, 50]"></vue-timepicker>
<!-- >> Active Items: 00, 06, 10, 11, 12, 13, ..., 27, 28, 29, 30, 42, 50 -->

<!-- Second range -->
<vue-timepicker format="H:m:s" :second-range="[0, 6, [10, 30], 42, 50]"></vue-timepicker>
<!-- >> Active Items: 0, 6, 10, 11, 12, 13, ..., 27, 28, 29, 30, 42, 50 -->
```

When implemented together with `minute-interval` and `second-interval`, the customized intervals take the priority.

```html
<!-- Minute range + 5-minute interval -->
<vue-timepicker :minute-range="[0, 6, [10, 30], 42, 50]" :minute-interval="5"></vue-timepicker>
<!-- >> Active Items: 00, 10, 15, 20, 25, 30, 50 -->

<!-- Second range + 10-second interval-->
<vue-timepicker format="H:m:s" :second-range="[0, 6, [10, 30], 42, 50]" :second-interval="10"></vue-timepicker>
<!-- >> Active Items: 0, 10, 20, 30, 50 -->
```

### Hide Disabled Items

There're four kinds of helper properties to let you hide the values excluded by `hour-range`, `minute-range`, and `second-range`.

- **hide-disabled-items**: Hide **all** disabled items - hour, minute, and seconds.
- **hide-disabled-hours**: Hide disabled **hour** values only.
- **hide-disabled-minutes**: Hide disabled **minute** values only.
- **hide-disabled-seconds**: Hide disabled **second** values only.

```html
<!-- `hide-disabled-hours` sample -->
<vue-timepicker :hour-range="[5, [8, 12], [14, 17], 19]" hide-disabled-hours></vue-timepicker>
```

Here we take the `hide-disabled-hours` as an example. It's a pair with the `hour-range` parameter. In this case, the hour picker hides the invalid hours (_0, 1, 2, 3, 4, 6, 7, 13, 18, 20, 21, 22, 23_) and display the valid hours (_5, 8, 9, ..._) only.

### Advanced Keyboard Support

Basic keyboard support includes:

- **Tab**: Focus or blur the Timepicker
- **Esc**: Close the dropdown

Advance Keyboard support (enabled with `advanced-keyboard`):

- **Arrow Keys**: Navigate between valid (non-disabled) values and columns
- **Space** or **Enter**: Select the focusing item

```html
<vue-timepicker advanced-keyboard></vue-timepicker>
```

Please be aware that after putting the `advanced-keyboard` on, hundreds of additional keyboard event listeners are going to be attached to the component. The amount of listeners depends on how many hours, minutes, and seconds value you enabled in the current Timepicker.

### Blur Delay

```html
<!-- Unit: million second -->
<vue-timepicker :blur-delay="500"></vue-timepicker>
```

Sets the blur delay time for the dropdown. Defaults to `300` if not set.

### Manual Input Support

```html
<vue-timepicker manual-input></vue-timepicker>
```
Let users add or change values through the `<input>` box besides the dropdown picker.

### Manual Input Timeout

```html
<!-- Unit: million second -->
<vue-timepicker :manual-input-timeout="1500"></vue-timepicker>
```

Works with **manual-input** mode. It sets the timeout for continuous input. Defaults to `1000` if not set.

**How It Works?**

For example, when a user focuses on the **hour** slot (`HH`) of a `"HH:mm"` formatted Timepicker (with the default value `1000`):

- **Case 1:** User first inputs `1`, and then inputs `2` _500ms_ later -> Timepicker takes `12` as the final value and set it to the `"HH"` slot.
- **Case 2:** User inputs `1`, and then presses the key `2` _1200ms_ later -> Timepicker takes `2` as the final value and set it to `02` for the `"HH"` slot.

### Hide Dropdown

> **NOTE:** To use this feature, you MUST ENABLE the `manual-input` mode _(v.1.1.0+)_ in the first place.

It makes the dropdown picker hidden by default.

```html
<vue-timepicker manual-input hide-dropdown></vue-timepicker>
```

Users can still choose to open the dropdown by clicking the triangle ("&dtrif;") button on the right. _(v.1.1.3+)_

### Fixed Dropdown Button

```html
<vue-timepicker fixed-dropdown-button></vue-timepicker>
```

Make the dropdown button always visible in the UI. _(v.1.1.4+)_

### Drop Direction

Change dropdown direction when needed _(v.1.1.5+)_. Accepting values:

- **down**: Default value.
- **up**: Force open the dropdown above the input.
- **auto**: Auto detects available height and opens the dropdown on top if there are not enough spaces below the input.

```html
<!-- Force drop up -->
<vue-timepicker drop-direction="up"></vue-timepicker>

<!-- Auto drop direction  -->
<vue-timepicker drop-direction="auto"></vue-timepicker>
```

#### Container ID

Works with `drop-direction="auto"`. It defines the parent container where the timepicker should calculate the free spaces from. If this value is not set, timepicker will watch `document.body` instead.

```html
<!-- Parent Container ID: "auto-dropdown-containter" -->
<div id="auto-dropdown-containter">
  <!-- Defined Container -->
  <vue-timepicker drop-direction="auto" container-id="auto-dropdown-containter"></vue-timepicker>

  <!-- Default (document body) -->
  <vue-timepicker drop-direction="auto"></vue-timepicker>
</div>
```

#### Drop Offset Height

Works with `drop-direction="auto"` either. Defaults to `160` (unit: _px_) if the value is not set.

```html
<!--
  When the available bottom space is less than 200px,
  open the dropdown above the input.
-->
<vue-timepicker drop-direction="auto" :drop-offset-height="200"></vue-timepicker>
```

### Lazy Event Mode

```html
<vue-timepicker lazy></vue-timepicker>
```

When `lazy` event mode is toggled on, only an actual user behavior can trigger the `input` and `change` events. Which are:

- The user opened the dropdown and picked a new value
- The user clicked the ("&times;") clear button
- The user inputted a new value or clear the existing value in the Manual Input mode

In other words, on `lazy` mode, Timepicker won't emit `input` and `change` events on mounted, nor after the value got modified programmatically.


### Append To Body

Append the dropdown menu to the end of the document `<body>`. Try this if you have `z-index` or `overflow` layout issue with the dropdown.

```html
<vue-timepicker append-to-body></vue-timepicker>
```

The body-appended dropdown's CSS class is `vue__time-picker-dropdown`. Its default `z-index` is `100`. You can change the value by adding the following style in your app -- 

```css
/* E.g. set the z-index to 5000 */
.vue__time-picker-dropdown {
  z-index: 5000;
}
```

**NOTE**: If you have to override some of the CSS styles within the dropdown, you will need to update their selectors' class names as well. Simply change any `.vue__time-picker .dropdown` selector to `.vue__time-picker-dropdown`.

For example, when you have a customized background color set for selected values:

```css
/* Default override (not using "append-to-body") */
.vue__time-picker .dropdown ul li:not([disabled]).active {
  background: steelblue;
}

/* When using "append-to-body" */
.vue__time-picker-dropdown ul li:not([disabled]).active {
  background: steelblue;
}
```

### Enable Debug Mode

```html
<vue-timepicker debug-mode></vue-timepicker>
```

It's aimed to help developers to investigate the input -> output process. When debug mode is toggled **on**, you can see extra `DEBUG: ...` logs coming through the console window as you interact with the vue-timepicker.

Let's create a "bug" here as an example --

```html
<!-- Manual Bug Sample: Define timepicker with format "h:mm:ss A" -->
<vue-timepicker v-model="yourStringValue" format="h:mm:ss A" debug-mode></vue-timepicker>
```

```javascript
{
  data () {
    return {
      // Manual Bug Sample:
      // Should be '3:mm:05 A' but oops.. the finger slipped
      yourStringValue: 'e:mm:05 A'
    }
  }
}
```

Then, in the console window, you should see a debug log saying:

```console
DEBUG: The input string in "v-model" does NOT match the "format" pattern
format: h:mm:ss A
v-model: e:mm:05 A
```

## Main Props API Overview

Prop                      | Type               | Required | Default Value
------------------------- | ------------------ | -------- | -------------
**v-model**               | _Object_, _String_ | no       | _undefined_
**format**                | _String_           | no       | "HH:mm"
**minute-interval**       | _Number_           | no       | _undefined_
**second-interval**       | _Number_           | no       | _undefined_
**hide-clear-button**     | _Boolean_          | no       | false
**disabled**              | _Boolean_          | no       | false
**close-on-complete**     | _Boolean_          | no       | false
**auto-scroll**           | _Boolean_          | no       | false
**hour-range**            | _Array_            | no       | _undefined_
**minute-range**          | _Array_            | no       | _undefined_
**second-range**          | _Array_            | no       | _undefined_
**hide-disabled-hours**   | _Boolean_          | no       | false
**hide-disabled-minutes** | _Boolean_          | no       | false
**hide-disabled-seconds** | _Boolean_          | no       | false
**hide-disabled-items**   | _Boolean_          | no       | false
**advanced-keyboard**     | _Boolean_          | no       | false
**blur-delay**            | _Number_           | no       | 300
**manual-input**          | _Boolean_          | no       | false
**manual-input-timeout**  | _Number_           | no       | 1000
**hide-dropdown**         | _Boolean_          | no       | false
**fixed-dropdown-button** | _Boolean_          | no       | false
**drop-direction**        | _String_           | no       | "down"
**container-id**          | _String_           | no       | _undefined_
**drop-offset-height**    | _Number_           | no       | 160
**lazy**                  | _Boolean_          | no       | false
**append-to-body**        | _Boolean_          | no       | false
**debug-mode**            | _Boolean_          | no       | false


## Input Props API

Prop              | Type                        | Required | Default Value
------------------| --------------------------- | -------- | -------------
**id**            | _String_                    | no       | _undefined_
**name**          | _String_                    | no       | _undefined_
**placeholder**   | _String_                    | no       | _undefined_
**tabindex**      | _Number_                    | no       | 0
**autocomplete**  | _String_                    | no       | 'off'
**input-class**   | _String_, _Array_, _Object_ | no       | _undefined_
**input-width**   | _String_                    | no       | '10em'

Timepicker supports `id`, `name`, `placeholder`, and `tabindex` like common form elements. These values are assigned to the `<input type="text" class="display-time">` within the component.

### Input `id`, `name` and `tabindex`

```html
<!-- id -->
<vue-timepicker id="myFirstPicker"></vue-timepicker>

<!-- name -->
<vue-timepicker name="nameInForm"></vue-timepicker>

<!-- tabindex -->
<vue-timepicker :tabindex="5"></vue-timepicker>
```

### Input `placeholder`

When `placeholder` is undefined, timepicker takes the determined format string instead.

```html
<!-- placeholder is set -->
<vue-timepicker placeholder="Start Time"></vue-timepicker>
<!-- -> "Start Time" -->

<!-- placeholder not set -->
<vue-timepicker format="hh:mm A"></vue-timepicker>
<!-- -> "hh:mm A" -->

<!-- both placeholder and format are not set -->
<vue-timepicker></vue-timepicker>
<!-- -> "HH:mm" -->
```

### Input `autocomplete` Attribute

> **NOTE:** To use this property, you MUST ENABLE the `manual-input` mode _(v.1.1.0+)_ in the first place.

```html
<!-- In Vue Template -->
<vue-timepicker name="starttime" autocomplete="on" manual-input></vue-timepicker>
```

```html
<!-- HTML result -->
<span class="vue__time-picker time-picker">
  <input class="display-time" name="starttime" type="text" autocomplete="on">
  <!-- ... -->
</span>
```

When enabled, it accepts any string value supported by the HTML input `autocomplete` attribute. The value is assigned to the embedding text `<input>`, which means it follows form autofill rules and configs set in the browser level. For example, most of the browsers require the input to have a `name` and/or `id` attribute. Some browsers, like Firefox, demand the input to be a descendant of a `<form>` element.

Please refer to the [HTML documentation](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill) and the developer guideline of each browser for more information (i.e., [MDN docs here](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete)).


### The `input-class`

The `input-class` is assigned to the text input within the component as well.

```html
<!-- Set your own `input-class` in the Vue template -->
<vue-timepicker input-class="my-awesome-picker"></vue-timepicker>
```

```html
<!-- HTML result -->
<span class="vue__time-picker time-picker">
  <input class="display-time my-awesome-picker" type="text" readonly="readonly">
  <!-- ... -->
</span>
```

Start from `v1.0.4`, besides _String_ format, `input-class` accepts value in _Array_ and _Object_ type as well.

```html
<!-- String type -->
<vue-timepicker input-class="your-awesome-timepicker i-am-vue2-timepicker"></vue-timepicker>

<!-- Array type -->
<vue-timepicker :input-class="['your-awesome-timepicker', 'i-am-vue2-timepicker']"></vue-timepicker>

<!-- Object type -->
<vue-timepicker :input-class="{
  'your-awesome-timepicker': true,
  'foo': false,
  'i-am-vue2-timepicker': true,
  'bar': false
}"></vue-timepicker>
```

```html
<!-- All of the three samples above return the same result in rendered HTML -->
<span class="vue__time-picker time-picker">
  <input class="display-time your-awesome-timepicker i-am-vue2-timepicker" type="text" readonly="readonly">
  <!-- ... -->
</span>
```

### The `input-width`

The `input-width` helps you to adjust both the `<input>` and the dropdown picker's width without overriding the CSS style on your own. It accepts any valid CSS width values like `8em`, `200px`, etc.

```html
<!-- In `px` -->
<vue-timepicker input-width="100px"></vue-timepicker>

<!-- In `em` -->
<vue-timepicker input-width="12em" format="HH:mm:ss"></vue-timepicker>
```


## Events API

Event          | Arguments      | Description
-------------- | -------------- | ----------------------
**input**      | (_value_)      | Emit after value changes
**change**     | (_eventData_)  | Emit after value changes
**open**       | &nbsp;         | Emit when the dropdown opens
**close**      | (_eventData_)  | Emit when the dropdown closes
**focus**      | &nbsp;         | Emit when the user start focusing on the `<input>`
**blur**       | (_eventData_)  | Emit when the user blurs the `<input>`
**error**      | (_eventData_)  | Emit when the input value becomes invalid

### The `open` and `close` Event of the Dropdown Picker

Help to identify the current status of the dropdown picker

```javascript
data () {
  return {
    dropdownStatus: 'closed'
  }
}
```

```html
<p>Dropdown Status: I'm {{dropdownStatus}}!</p>

<vue-timepicker @open="dropdownStatus = 'opened'" @close="dropdownStatus = 'closed'"></vue-timepicker>
```

### The `focus` and `blur` Event

It works with the Manual Input mode, aimed to identify the focus/blur state of the `<input>` box. Specially useful in cases where the dropdown is force hidden by `hide-dropdown`.

```javascript
data () {
  return {
    focusState: 'blurred'
  }
}
```

```html
<p>Focus State: {{focusState}}</p>

<vue-timepicker manual-input hide-dropdown @focus="focusState = 'focused'" @blur="focusState = 'blurred'"></vue-timepicker>
```

### The `error` event

Starts from `v.1.1.0+`, Timepicker will emit an `error` event when the current input value becomes invalid. E.g., when it contains an hour value that is not in the `hour-range` list or a minute value that doesn't fit in the `minute-interval`.

```html
<!-- Got the `hour-range` and `minute-interval` set -->
<!-- And add a hanlder to pick up the "error" event -->
<vue-timepicker format="H:mm:ss" v-model="erroredInputSample" :hour-range="[8, 9, 10, 11]" :minute-interval="5" @error="errorHanlder"></vue-timepicker>
```

```javascript
data () {
  return {
    erroredInputSample: { H: '5', mm: '03', ss: '00' }
    // NOTE:
    // H: '5' -> invalid. Value is not in the `hour-range` list
    // mm: '03' -> invalid. Value does not fit in the `minute-interval`
    // ss: '00' -> valid.
  }
},

methods: {
  errorHanlder (eventData) {
    console.log(eventData)
    // console.log outputs -> ["hour", "minute"]
  }
}
```

The `error` event returns an _Array_ of invalid fields' names. When it returns an empty array `[]`, it means the current input is valid, and all previous errors are gone

> NOTE: Empty value will **not** be marked as invalid.


## Helper CSS Class Names

Started from `v.1.1.0+`, Vue Timepicker will add additional CSS classes to the `<input>` element base on the state of the current input value.

- **invalid**: One or more fields containing an invalid or disabled value.
  - Additional CSS Style: The `<input>` border turns red.
  - If you want to mute this red border style, add `"skip-error-style"` to `input-class`
- **is-empty**: The input value (_v-model_) is empty. No additional style.
- **all-selected**: All fields (hour/minute/second/apm) required by the `format` string are not empty. No additional style.

```html
<!-- To mute the red border style of "invalid" state -->
<timepicker input-class="skip-error-style"></timepicker>
<timepicker :input-class="['skip-error-style', 'your-other-class-names']"></timepicker>
```


## Miscellaneous Props API

Prop                    | Type      | Required | Default Value
----------------------- | --------- | -------- | -------------
**hour-label**          | _String_  | no       | _undefined_
**minute-label**        | _String_  | no       | _undefined_
**second-label**        | _String_  | no       | _undefined_
**apm-label**           | _String_  | no       | _undefined_
**am-text**             | _String_  | no       | _undefined_
**pm-text**             | _String_  | no       | _undefined_

### Customized Picker Labels

You can define customized labels on top of the hour, minute, second, and APM pickers with the following properties: `hour-label`, `minute-label`, `second-label`, and `apm-label`. 

Furthermore, you can replace those _am/pm_ (or _AM/PM_) string by setting the `am-text` and `pm-text` parameters.

> Please note that these two parameters only change the labels expose to the users (the UI level). The `v-model` value and `displayTime` value returned by the `change` event (the data level) still use the standard _am_/_pm_ (_AM_/_PM_) format.

```html
<!-- 24-hour format with customized hour and minute label -->
<vue-timepicker hour-label="heure" minute-label="minute"></vue-timepicker>

<!-- 12-hour format with customized am/pm text -->
<vue-timepicker hour-label="時" minute-label="分" second-label="秒" apm-label="午" am-text="上午" pm-text="下午" format="h:mm:ss a"></vue-timepicker>
```


## Slots

We introduce three slots in `v.1.1.4` to help you customize the clear button, the dropdown button, and the input icon with your own icon/image.

Slot Name          | Position | Description   
------------------ | -------- | --------------
**icon**           | _left_   | On the lefthand side of the `<input>`
**clearButton**    | _right_  | In the same spot of the default clear button
**dropdownButton** | _right_  | In the same spot of the default dropdown button

> Please note that Vue v2.6.0+ introduces a significant update of the Named Slots syntax. Check the [official documentation](https://vuejs.org/v2/guide/components-slots.html#Named-Slots) for more information.

```html
<!-- For Vue 2.6.0+ -->

<!-- Input icon (image) -->
<vue-timepicker>
  <template v-slot:icon>
    <img src="$YOUR_ICON_SRC" />
  </template>
</vue-timepicker>

<!-- Customized clear button (image) -->
<vue-timepicker>
  <template v-slot:clearButton>
    <img src="$YOUR_CUSTOM_IMAGE_SRC" />
  </template>
</vue-timepicker>

<!-- Customized dropdown button (character entity) -->
<vue-timepicker manual-input hide-dropdown>
  <template v-slot:dropdownButton>&#x02263;</template>
</vue-timepicker>
```

## Contribution

Please feel free to fork and help developing. Check [CONTRIBUTING.md](https://github.com/phoenixwong/vue2-timepicker/blob/master/CONTRIBUTING.md) for more details.

## Change Log

Detail changes of each release: [CHANGELOG.md](https://github.com/phoenixwong/vue2-timepicker/blob/master/CHANGELOG.md)

## License

[MIT](https://github.com/phoenixwong/vue2-timepicker/blob/master/LICENSE.md)
