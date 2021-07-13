<table>
<tr>
	<td> <img src="http://enisnecipoglu.com/Plugins/inputkit.png" width="120" /></td>
	<td> 
		<h1> Xamarin.Forms.InputKit </h1>
		<p><a href="https://github.com/enisn/Xamarin.Forms.InputKit/wiki/CheckBox">CheckBox</a>, Radio Button, Advanced Entry, Advanced Slider, Dropdown etc.  </p> 
	</td>
</tr>
</table>


<hr />

[![Build status](https://ci.appveyor.com/api/projects/status/st6lcbts9bkhxqub?svg=true)](https://ci.appveyor.com/project/enisn/xamarin-forms-inputkit)
[![CodeFactor](https://www.codefactor.io/repository/github/enisn/xamarin.forms.inputkit/badge)](https://www.codefactor.io/repository/github/enisn/xamarin.forms.inputkit)
[![Nuget](https://img.shields.io/nuget/v/Xamarin.Forms.InputKit)](https://www.nuget.org/packages/Xamarin.Forms.InputKit/)
![Nuget](https://img.shields.io/nuget/dt/Xamarin.Forms.InputKit?logo=nuget)
<a href="https://github.com/enisn/Xamarin.Forms.InputKit/wiki"> <img src="https://img.shields.io/badge/Visit-WiKi-orange.svg"/></a>
<br />
[![Sparkline](https://stars.medv.io/enisn/Xamarin.Forms.InputKit.svg)](https://stars.medv.io/enisn/Xamarin.Forms.InputKit)
<hr/>


 ## Available Platforms

| Platform | Version | Supported |
| --- | --- | --- |
| Android | MonoAndroid 11.0 | ✅ |
| Android | MonoAndroid10.0 | ✅ |
| Android | MonoAndroid90 | ✅ |
| Android | MonoAndroid81 | ❌ \| InputKit v2.x |
| iOS | Xamarin.iOS10 | ✅ |
| UWP | - | **EXPERIMENTAL** |
| MAC | Xamarin.Mac20 | ✅ |
| WatchOS | Xamarin.WatchOS10 | ⚠ |
| .NET Standard | 2.0 | ✅ |
| .NET Standard | 1.0 | ✅ |

<hr/>

## Getting Started with InputKit

There is no complicated steps for set-up, no Inits no implementation codes. Plug & Play.

Read [Documentation of Getting Started](https://github.com/enisn/Xamarin.Forms.InputKit/wiki/Getting-Started).

<hr />

<a href="https://github.com/enisn/Xamarin.Forms.InputKit/wiki/CheckBox">
<h2>Checkbox</h2>
</a>
<p>As you know ther is no CheckBox in Xamarin Forms Library. You can use a custom renderer to use Native Checkbox in portable layer. This CheckBox is not a native one, It's created in Xamarin Forms Portable layer.</p>

<p>Also you can read more about Checkbox from <a href="https://github.com/enisn/Xamarin.Forms.InputKit/wiki/CheckBox">here</a> </p>
<h4>SAMPLE:</h4>

```xaml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:local="clr-namespace:Sample.InputKit"
             xmlns:input="clr-namespace:Plugin.InputKit.Shared.Controls;assembly=Plugin.InputKit"
             x:Class="Sample.InputKit.MainPage">
        <StackLayout Spacing="12" Padding="30,0">
            <input:CheckBox Text="Option 1" Type="Box" />
            <input:CheckBox Text="Hello World I'm Option 2" Type="Check"/>
            <input:CheckBox Text="Consetetur eum kasd eos dolore Option 3" Type="Cross"/>
            <input:CheckBox Text="Sea sed justo" Type="Star"/>
        </StackLayout>
</ContentPage>
```
<br />
<table>
<tr>
<td>
<img src="https://raw.githubusercontent.com/enisn/Xamarin.Forms.InputKit/develop/shreenshots/checkboxes_android.gif" alt="Xamarin Forms CheckBox Input Kit Enis Necipoglu" width="270" height="480" class="aligncenter size-medium wp-image-996" />
</td>
<td>
<img src="https://raw.githubusercontent.com/enisn/Xamarin.Forms.InputKit/develop/shreenshots/checkboxes_ios.png" alt="Xamarin Forms CheckBox Input Kit Enis Necipoglu" width="270" height="480" class="aligncenter size-medium wp-image-996" />
</td>
</tr>
</table>

<h4>PROPERTIES:</h4>
<ul>
	<li><strong>CheckChanged:</strong> <em>(Event)</em> Invokes when check changed.</li>
        <li><strong>CheckChangedCommand:</strong> <em>(Command)</em> Bindable Command, executed when check changed.</li>
        <li><strong>Key:</strong> <em>(int)</em> A key you can set to define checkboxes as ID.</li>
 <li><strong>Text:</strong> <em>(string)</em> Text to display description</li>
<li><strong>IsChecked:</strong> <em>(bool)</em> Checkbox checked situation. Works TwoWay Binding as default.</li>
<li><strong>Color:</strong> <em>(Color)</em> Color of selected check.</li>
<li><strong>TextColor:</strong> <em>(Color)</em> Color of description text.</li>
<li><strong>Type:</strong> <em>(CheckType)</em> Type of checkbox checked style. (Check,Cross,Star,Box etc.)</li>
</ul>
<hr />


<h2>RadioButon</h2>
<p>Radio Buttons should use inside a <strong>RadioButtonGroupView</strong>. If you want this view will return you selected radio button. But you can handle it one by one too. </p>
<h4>SAMPLE:</h4>

```xaml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
            xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
            xmlns:local="clr-namespace:Sample.InputKit"
            xmlns:input="clr-namespace:Plugin.InputKit.Shared.Controls;assembly=Plugin.InputKit"
            x:Class="Sample.InputKit.MainPage">

        <StackLayout Spacing="12" Padding="30,0">

            <input:RadioButtonGroupView>
                <input:RadioButton Text="Option 1" />
                <input:RadioButton Text="Option 2" />
                <input:RadioButton Text="Option 3" />
                <input:RadioButton Text="Option 4" />
            </input:RadioButtonGroupView>

        </StackLayout>

</ContentPage>
```

<table>
<tr>
<td>
<img src="https://raw.githubusercontent.com/enisn/Xamarin.Forms.InputKit/develop/shreenshots/radiobuttons_android.gif" alt="Xamarin Forms Radio Button Input Kit Enis Necipoğlu" width="270" height="480" class="aligncenter size-medium wp-image-1001" />
</td>
<td>
<img src="https://raw.githubusercontent.com/enisn/Xamarin.Forms.InputKit/develop/shreenshots/radiobuttons_ios.png" alt="Xamarin Forms Radio Button Input Kit Enis Necipoğlu" width="270" height="480" class="aligncenter size-medium wp-image-1001" />
</td>
</tr>
</table>
<h4>PROPERTIES:</h4>
<h5>RadioButtonGroupView</h5>
<ul>
<li><strong>SelectedIndex:</strong> <em>(int)</em> Gets or Sets selected radio button inside itself by index</li>
<li><strong>SelectedItem:</strong> <em>(object)</em> Gets or Sets selected radio button inside itself by Value</li>
</ul>
<h5>RadioButton</h5>
<ul>
<li><strong>Clicked:</strong> <em>(event)</em> Invokes when clikced</li>
<li><strong>ClickCommand:</strong> <em>(int)</em> Bindable Command, Executes when clicked</li>
<li><strong>Value:</strong> <em>(object)</em> A value keeps inside and groupview returns that value as SelectedItem</li>
<li><strong>IsChecked:</strong> <em>(bool)</em> Gets or Sets that radio button selected</li>
<li><strong>Text:</strong> <em>(string)</em> Text to display near of Radio Button</li>
<li><strong>TextFontSize:</strong> <em>(double)</em> Fontsize of Text</li>
<li><strong>Color:</strong> <em>(Color)</em> Color of selected radio button dot</li>
<li><strong>TextColor:</strong> <em>(Color)</em> Color of Text</li>
</ul>
<hr />
<hr />


<h2>AutoCompleteEntry ( Experimental )</h2>
<p>Alternative picker with dropdown menu.
</p>
<h4>SAMPLE:</h4>

```xaml
 <input:AutoCompleteEntry Title="Type something below:"
                          ItemsSource="{Binding MyList}" 
                          SelectedItem="{Binding SelectedItem}" />
```

<table>
<tr>
<td>
<a href="#"><img src="https://raw.githubusercontent.com/enisn/Xamarin.Forms.InputKit/develop/shreenshots/autocompleteentries_android.gif" width="270" height="480" alt="Xamarin Forms Slider Sticky Label" class="aligncenter size-medium" /></a>
</td>
<td>
<a href="#"><img src="https://raw.githubusercontent.com/enisn/Xamarin.Forms.InputKit/develop/shreenshots/autocompleteentries_ios.png" width="270" height="480" alt="Xamarin Forms Slider Sticky Label" class="aligncenter size-medium" /></a>
</td>
</tr>
</table>

<h4>PROPERTIES:</h4>
<ul>
<li><strong>Placeholder:</strong> <em>(string)</em> Placehodler Text</li>
<li><strong>Title:</strong> <em>(string)</em> Title will be shown top of this control</li>
<li><strong>IconImage:</strong> <em>(string)</em> Icons of this Entry. Icon will be shown left of this control</li>
<li><strong>Color:</strong> <em>(Color)</em> Color of Icon Image. IconImage must be a PNG and have Alpha channels. This fills all not-Alpha channels one color. <i>Default is Accent</i></li>
<li><strong>ValidationMessage:</strong> <em>(string)</em> This is message automaticly displayed when this is not validated. **Use this one instead of annotationmessage**</li>
<li><strong>AnnotationColor:</strong> <em>(Color)</em> AnnotationMessage's color..</li>
<li><strong>IsRequired:</strong> <em>(bool)</em> IValidation implementation. Same with IsAnnotated</li>
<li><strong>ItemsSource:</strong> <em>(IList)</em> Suggestions items</li>
</ul>

To be added...
<hr />

<h2>Dropdown ( Experimental  * Not Stable * )</h2>
<p>Alternative picker with dropdown menu.
</p>
<h4>SAMPLE:</h4>

```xaml
 <input:Dropdown Title="Chosse an option below:"
                            TitleColor="Black"
                            ValidationMessage="This field is required" 
                            AnnotationColor="Accent" 
                            IsRequired="True" 
                            BorderColor="Black" 
                            Color="BlueViolet"
                            Placeholder="Choose one" 
                            ItemsSource="{Binding MyList}" 
                            SelectedItem="{Binding SelectedItem}" />
```
<a href="#"><img src="https://media.giphy.com/media/CjGR8p3HoeOup8r21J/giphy.gif" width="270" height="480" alt="Xamarin Forms Slider Sticky Label" class="aligncenter size-medium" /></a>

<h4>PROPERTIES:</h4>
<ul>
<li><strong>Placeholder:</strong> <em>(string)</em> Placehodler Text</li>
<li><strong>Title:</strong> <em>(string)</em> Title will be shown top of this control</li>
<li><strong>IconImage:</strong> <em>(string)</em> Icons of this Entry. Icon will be shown left of this control</li>
<li><strong>Color:</strong> <em>(Color)</em> Color of Icon Image. IconImage must be a PNG and have Alpha channels. This fills all not-Alpha channels one color. <i>Default is Accent</i></li>
<li><strong>ValidationMessage:</strong> <em>(string)</em> This is message automaticly displayed when this is not validated. **Use this one instead of annotationmessage**</li>
<li><strong>AnnotationColor:</strong> <em>(Color)</em> AnnotationMessage's color..</li>
<li><strong>IsRequired:</strong> <em>(bool)</em> IValidation implementation. Same with IsAnnotated</li>
</ul>

To be adde...
<hr />



<hr />
<h2>Advanced Entry</h2>
<p>This entry has many features to develop your applications quickly. When this entry completed, it finds next entry in Parent layout and focus it. AdvancedEntry contains validation system inside it. You can set some properties to validate it and you can handle all your entries is validated or not with **FormView**.
You can set validation message and AnnotatinColor. Entry will automaticly display your message when it's not validated.
</p>
<h4>SAMPLE:</h4>

```xaml
 <StackLayout Padding="30">
            <Label Text="You can see FormView Below:"/>
            <BoxView HeightRequest="1" Color="LightGray" />
            <input:FormView IsValidated="{Binding IsValidated}">
                
                <input:AdvancedEntry 
                    Text="{Binding Email}"
                    IsRequired="True"
                    Title="Place your email below:"
                    Annotation="Email"
                    Placeholder="sample@domain.com"
                    AnnotationColor="Accent"
                    ValidationMessage="Please type a valid email address"
                    IconImage="ic_email_black_24dp.png"
                    MinLength="10"
                    MaxLength="50"
                    />

                <input:AdvancedEntry 
                    Text="{Binding NameSurname}"
                    IsRequired="True"
                    Title="Place your name below:"
                    Annotation="NameSurname"
                    Placeholder="John Doe"
                    AnnotationColor="Accent"
                    ValidationMessage="Please type your name correctly"
                    IconImage="ic_account_circle_black_24dp.png"
                    MinLength="5"
                    MaxLength="30"
                    />

                <input:AdvancedEntry 
                    Text="{Binding Phone}"
                    IsRequired="True"
                    Title="Place your phone number below:"
                    Annotation="Phone"
                    Placeholder="5439998877"
                    AnnotationColor="Accent"
                    ValidationMessage="Please type your phone number correctly"
                    IconImage="ic_account_circle_black_24dp.png"
                    MaxLength="10"
                    />

                <Button Command="{Binding SubmitCommand}" Text="Submit" BackgroundColor="Accent" CornerRadius="20" TextColor="White" />
            </input:FormView>
        </StackLayout>
```
<a href="#"><img src="https://media.giphy.com/media/1zl0u7O2doNolIXnrT/giphy.gif" width="270" height="480" alt="Xamarin Forms Slider Sticky Label" class="aligncenter size-medium" /></a>

<h4>PROPERTIES:</h4>
<ul>
<li><strong>Text:</strong> <em>(string)</em> Text of user typed</li>
<li><strong>Title:</strong> <em>(string)</em> Title will be shown top of this control</li>
<li><strong>IconImage:</strong> <em>(string)</em> Icons of this Entry. Icon will be shown left of this control</li>
<li><strong>IconColor:</strong> <em>(Color)</em> Color of Icon Image. IconImage must be a PNG and have Alpha channels. This fills all not-Alpha channels one color. <i>Default is Accent</i></li>
<li><strong>Placeholder:</strong> <em>(string)</em> Entry's placeholder.</li>
<li><strong>MaxLength:</strong> <em>(int)</em> Text's Maximum length can user type.</li>
<li><strong>MinLength:</strong> <em>(int)</em> Text's Minimum length to be validated.</li>
<li><strong>AnnotationMessage:</strong> <em>(string)</em> This will be shown below title. This automaticly updating. If you set this manually you must set true IgnoreValidationMessage !!!  .</li>
<li><strong>AnnotationColor:</strong> <em>(Color)</em> AnnotationMessage's color..</li>
<li><strong>Annotation:</strong> <em>(Enum)</em> There is some annotation types inside in kit.</li>
<li><strong>IsDisabled:</strong> <em>(bool)</em> Sets this control disabled or not.</li>
<li><strong>IsAnnotated:</strong> <em>(bool)</em> Gets this control annotated or not. Depends on Annotation</li>
<li><strong>IsRequired:</strong> <em>(bool)</em> IValidation implementation. Same with IsAnnotated</li>
<li><strong>ValidationMessage:</strong> <em>(string)</em> This is message automaticly displayed when this is not validated. **Use this one instead of annotationmessage**</li>
<li><strong>IgnoreValidationMessage:</strong> <em>(bool)</em> Ignores automaticly shown ValidationMessage and you can use AnnotationMessage as custom. </li>
<li><strong>CompletedCommand:</strong> <em>(ICommand)</em> Executed when completed. </li>
</ul>
<hr />



<h2>Advanced Slider</h2>
<p>Xamarin Forms Slider works a Sticky label on it. Wonderful experience for your users.</p>
<h4>SAMPLE:</h4>

```xaml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:local="clr-namespace:Sample.InputKit"
             xmlns:input="clr-namespace:Plugin.InputKit.Shared.Controls;assembly=Plugin.InputKit"
             x:Class="Sample.InputKit.MainPage">

    <StackLayout Spacing="12" Padding="10,0" VerticalOptions="CenterAndExpand">

        <input:AdvancedSlider MaxValue="5000" MinValue="50" StepValue="50" ValuePrefix="Price:" ValueSuffix="€" Title="Choose Budget:"/>

    </StackLayout>

</ContentPage>
```
<a href="https://media.giphy.com/media/BoIPfRefA0Q9AtJ6mQ/giphy.gif"><img src="https://media.giphy.com/media/BoIPfRefA0Q9AtJ6mQ/giphy.gif" width="270" height="480" alt="Xamarin Forms Slider Sticky Label" class="aligncenter size-medium" /></a>

<h4>PROPERTIES:</h4>
<ul>
<li><strong>Value:</strong> <em>(double)</em> Current Selected Value, (this can be used TwoWayBinding)</li>
<li><strong>Title:</strong> <em>(string)</em> Title of slider</li>
<li><strong>ValueSuffix:</strong> <em>(string)</em> Suffix to be displayed near Value on Floating Label</li>
<li><strong>ValuePrefix:</strong> <em>(string)</em> Prefix to be displayed near Value on Floating Label</li>
<li><strong>MinValue:</strong> <em>(double)</em> Sliders' minimum value</li>
<li><strong>MaxValue:</strong> <em>(double)</em> Sliders' maximum value</li>
<li><strong>MaxValue:</strong> <em>(double)</em> Sliders' increment value</li>
<li><strong>TextColor:</strong> <em>(Color)</em> Color of Texts</li>
<li><strong>DisplayMinMaxValue:</strong> <em>(bool)</em> Visibility of Minimum and Maximum value</li>
</ul>
<hr />

<h2>SelectionView</h2>
<p>Presents options to user to choose. This view didn't created to static usage. You should Bind a model List as ItemSource, or if you don't use MVVM you can set in page's cs file like below. (You can override ToString method to fix display value or I'll add displayMember property soon.)</p>
<h4>SAMPLE:</h4>

```xaml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:local="clr-namespace:Sample.InputKit"
             xmlns:input="clr-namespace:Plugin.InputKit.Shared.Controls;assembly=Plugin.InputKit"
             x:Class="Sample.InputKit.MainPage">

    <StackLayout Spacing="12" Padding="10,0" VerticalOptions="CenterAndExpand">

        <input:SelectionView x:Name="selectionView" />

    </StackLayout>
</ContentPage>
```

```csharp
public partial class MainPage : ContentPage
	{
		public MainPage()
		{
			InitializeComponent();
            selectionView.ItemSource = new[]
            {
                "Option 1","Option 2","Option 3","Option 4","Option 5","Option 6","Option 7","Option 8"
            };
		}
	}
```

<a href="https://media.giphy.com/media/KXtC6oNnOgnJhvYecy/giphy.gif"><img src="https://media.giphy.com/media/KXtC6oNnOgnJhvYecy/giphy.gif" width="270" height="480" alt="Xamarin Forms SelectionView Enis Necipoglu" class="aligncenter size-medium" /></a>


You may use a object list as ItemSource, You can make this. Don't forget override **ToString()** method in your object.

sample object:

```csharp
  public class SampleClass
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public override string ToString() => Name;
    }
```

Usage:

```csharp
public partial class MainPage : ContentPage
	{
		public MainPage()
		{
			InitializeComponent();
           selectionView.ItemSource = new[]
            {
                new SampleClass{ Name = "Option 1", Id = 1 },
                new SampleClass{ Name = "Option 2", Id = 2 },
                new SampleClass{ Name = "Option 3", Id = 3 },
                new SampleClass{ Name = "Option 4", Id = 4 },
                new SampleClass{ Name = "Option 5", Id = 5 },
                new SampleClass{ Name = "Option 6", Id = 6 },
                new SampleClass{ Name = "Option 7", Id = 7 },
                new SampleClass{ Name = "Option 8", Id = 8 },
            };
		}
	}
```



<h4>PROPERTIES:</h4>
<ul>
<li><strong>ItemSource:</strong> <em>(IList)</em> List of options</li>
<li><strong>SelectedItem:</strong> <em>(object)</em> Selected Item from ItemSource</li>
<li><strong>ColumnNumber:</strong> <em>(int)</em> Number of columng of this view</li>
</ul>


<br />
<hr />

# Did you like ?

<a href="https://www.buymeacoffee.com/enisn" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

Your coffee keeps me awake while developing projects like this. 👍☕

<hr />

