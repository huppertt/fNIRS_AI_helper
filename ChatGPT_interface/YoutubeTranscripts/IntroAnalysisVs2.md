[00:00:00] my idea now is despite the fact that you
[00:00:04] spent the last hour and a half or
[00:00:05] whatever teaching you about all the
[00:00:07] coats that they existed in the past many
[00:00:10] of which I routes I'm now going to
[00:00:12] switch over to our new stuff and so
[00:00:16] we're going to walk through what's
[00:00:17] called the nearest toolbox the really
[00:00:19] creative name for our new that Pacific
[00:00:21] please
[00:00:22] this is needs to go back and forth so
[00:00:25] that you guys have questions if
[00:00:26] something's not clear please please ask
[00:00:28] and the goal here is to kind of walk you
[00:00:29] through some of the methods that how we
[00:00:33] do this in my toolbox and stuff when we
[00:00:37] can just find a little bit of the
[00:00:38] background of this it's it's kind of odd
[00:00:42] to come up in unit say we talked about
[00:00:44] Homer and how I use Homer and like yeah
[00:00:48] the the Homer was written in starting in
[00:00:53] about 2002 by me and David Louis as a
[00:00:57] means to analyze the data that we're
[00:00:59] collecting with our instruments your
[00:01:01] physicist was the exciting thing that we
[00:01:05] did about the brains if you have your
[00:01:07] fingers something happens over here and
[00:01:09] we were kind of interested in hardware
[00:01:13] development developing years we weren't
[00:01:15] necessarily asking the kind of questions
[00:01:17] said psychologists are the hypotheses
[00:01:20] method and so we wrote homer basically
[00:01:23] for our purposes we're testing out new
[00:01:26] methods and stuff like that at some
[00:01:29] point we realized that this was kind of
[00:01:31] a useful thing that people wanted some
[00:01:34] ended up making it open source and
[00:01:35] feeling it on but 15 years later or
[00:01:41] whatever now as as a professor and I
[00:01:44] worked at a lot of different groups and
[00:01:47] psychiatry and stuff the questions that
[00:01:50] were being asked you know people come to
[00:01:52] me that's like great we collected the
[00:01:54] data
[00:01:54] you show me a vintage the on condition a
[00:01:57] versus position the co-vary
[00:02:00] or age and gender treating visit as a
[00:02:05] random effect or something somebody you
[00:02:06] know something like that would be like
[00:02:08] no
[00:02:09] so let's do that and I realized that the
[00:02:12] methods that people really wanted or not
[00:02:16] the way that we had coded out homer and
[00:02:18] in fact actually even answer that
[00:02:20] question properly to do to make that
[00:02:22] image that my co-investigators wanted
[00:02:24] really meant I'm sorry Thomas it started
[00:02:28] about you really went going back to
[00:02:31] almost square one because the in order
[00:02:35] to answer that question I had to
[00:02:37] propagate all the information all the
[00:02:39] noise all day uncertainty through the
[00:02:41] models I had enough to make that the end
[00:02:43] to properly address that question and
[00:02:46] it's just the tools in Homer were not
[00:02:49] designed with that in mind they were
[00:02:51] designed it kind of evolved over time
[00:02:53] but from a base of a bunch of physicists
[00:02:56] sitting around having their fingers and
[00:02:58] so my student Jeff Barker who
[00:03:02] unfortunately was unable to keep in
[00:03:04] academia it's an awesome programmer and
[00:03:08] a great absolute great student my other
[00:03:12] PhD student dragged him away taking it
[00:03:15] to industry so they're making iPhone
[00:03:19] apps
[00:03:19] let's start up but Jeff originally wrote
[00:03:23] the your stool box that I'm gonna kind
[00:03:26] of show with kind of that idea in mind
[00:03:28] of knowing the end result knowing I want
[00:03:32] to address this hypothesis how do we
[00:03:34] propagate it all the information you
[00:03:37] need to that end so that we can we can
[00:03:39] do this or our collaborators and so
[00:03:42] that's kind of that the framework the
[00:03:44] nearest tool box is first and foremost
[00:03:47] focused on getting the stats right so it
[00:03:50] actually doesn't have a lot of those
[00:03:51] methods that I described early on of
[00:03:54] filtering and processing your data and
[00:03:56] pre-processing because it turns out that
[00:03:57] those are not actually truly essential
[00:03:59] to get the stats right and actually if
[00:04:02] you get the stats right a lot of those
[00:04:04] methods aren't even needed anymore with
[00:04:08] that with that said if they do help
[00:04:11] because having noise in your data is a
[00:04:14] bad thing if you had less noise you'd
[00:04:16] have better data but if your stats are
[00:04:18] dealt with correctly then you don't and
[00:04:21] you're able to
[00:04:23] void false discovery and avoid kind of
[00:04:26] those issues your results are still
[00:04:28] correct they'd be maybe better if you
[00:04:30] had less noise but you're not going to
[00:04:33] publish results that are false and so
[00:04:35] that was kind of the goal when your
[00:04:37] school box was to get the stats right so
[00:04:39] the nearest tool box lose its MATLAB
[00:04:42] written it's open source that's
[00:04:44] available on a site called bit pocket I
[00:04:47] do have all this kind of in PowerPoint
[00:04:50] with so don't try to jot down the
[00:04:53] finding words might have actually sent
[00:04:56] that link but if you go to the this
[00:04:58] bitbucket site you can find the nearest
[00:05:00] tool box here there's a the opening page
[00:05:06] is a wiki that i embarrassing lis
[00:05:09] haven't updated in quite a while
[00:05:11] but if you go to like download and
[00:05:13] installation computer actually works
[00:05:16] it'll bring you okay apparently I can't
[00:05:27] visit this on the URI Network but anyway
[00:05:29] you go to download installation it does
[00:05:32] have instructions for how to download
[00:05:34] this I'll walk that through in a second
[00:05:37] if you go through some of this like demo
[00:05:39] as an example is I've pasted some of the
[00:05:42] demos that I'm going through on this
[00:05:44] website that you can actually work
[00:05:46] through and it has a bit of information
[00:05:47] about the data structures and stuff it's
[00:05:50] actually the exact same data structure
[00:05:52] that that Homer uses so if and if you
[00:05:56] want to just download it quickly you can
[00:05:58] go to this page it's probably not gonna
[00:06:00] work either but this page here that says
[00:06:02] download and you say download toolbox
[00:06:04] and it checks it downloads the latest
[00:06:06] version yeah that's not gonna work
[00:06:09] but if you go to that on that wiki page
[00:06:11] with the downloads it has a little bit
[00:06:14] more detailed instructions because the
[00:06:17] advantage of of bitbucket
[00:06:18] is kind of like github or some of these
[00:06:21] other sites is it lets me continually
[00:06:24] make changes to my code and so if you
[00:06:28] want the latest greatest version because
[00:06:31] as I'm working through the example today
[00:06:32] I found a mistake that I fixed right
[00:06:34] here in front of you
[00:06:35] I can push those chain
[00:06:37] to the to the Internet and you can check
[00:06:39] out the latest version on your computer
[00:06:40] and so it has this and if you don't like
[00:06:43] those changes you can actually roll back
[00:06:44] to the version from February 2016 or
[00:06:48] whatever to keep a nice stable version
[00:06:50] for your stuff so bitbucket uses a
[00:06:53] program called new curio Mercurio is a
[00:06:57] way to manage those those things but if
[00:07:00] you download you go to that that
[00:07:02] instruction page it'll direct you to
[00:07:05] this program tour this HG and this is a
[00:07:08] nice program that installs on Windows or
[00:07:11] Mac computer where you just right-click
[00:07:14] on the folder and say update and it
[00:07:16] automatically updates with the latest
[00:07:18] version so it's it's a nice way to make
[00:07:21] sure you have the latest version of this
[00:07:24] with bitbucket there's also there's a
[00:07:29] way if you go to the website you can
[00:07:31] this is not gonna work again but you can
[00:07:35] file issues like hey Ted your program is
[00:07:39] just terrible please fix it you can
[00:07:42] submit that any getting email of you
[00:07:44] know with these requests and stuff like
[00:07:46] that and I can respond back with the
[00:07:48] website so if you do identify a bug or
[00:07:51] something like that sending it through
[00:07:52] the website is actually really nice and
[00:07:55] I I have a post doc that fixes it all
[00:07:59] the time in fact actually when I do this
[00:08:03] this is the tortoisehg and if you open
[00:08:06] it up on a Mac you open it up like here
[00:08:09] and you can just say update and
[00:08:12] apparently I don't have internet access
[00:08:15] anymore but what I would do is update
[00:08:18] the latest version it would tell me any
[00:08:19] changes it also keeps a history so it
[00:08:22] shows you that last night I fix the load
[00:08:25] function for the numerix format and
[00:08:28] added a stimulus group which is what I
[00:08:31] needed to do for the demo today so and
[00:08:33] actually this morning at 10 a.m. I know
[00:08:35] my post-doc updated something with
[00:08:37] branch of causality so but I haven't
[00:08:40] looked at it yet anyway the the toolbox
[00:08:43] is that I based it does
[00:08:46] unfortunately require a fairly new
[00:08:49] version of MATLAB
[00:08:50] 14 or above I say unfortunate because
[00:08:54] Homer requires 2013 or below so someone
[00:09:00] hit you both Homer in my code
[00:09:02] unfortunately YouTube versions in MATLAB
[00:09:03] I will try to fix that 2014 MATLAB we
[00:09:09] offered a release that introduced a
[00:09:11] bunch of new features that didn't
[00:09:14] previously exist and my toolbox so
[00:09:17] heavily relies on that that I can it
[00:09:20] won't work on the old version that also
[00:09:22] tells you that I've written this entire
[00:09:23] thing since late 2014 and there's
[00:09:26] something like two hundred thousand
[00:09:28] lines of code in there
[00:09:30] so anyway this that's go to this so the
[00:09:34] way the toolbox works is let's see if I
[00:09:40] can find data so it's it's it's MATLAB
[00:09:44] based and let's just go to the folder so
[00:09:51] inside of this this folder so this the
[00:09:54] nearest pillbox is this folder
[00:09:57] it contains a subfolder called demos so
[00:10:00] if you go into demos there is a bunch of
[00:10:08] demos MATLAB scripts that are fully
[00:10:11] functional that will show different
[00:10:13] demonstrate different features about the
[00:10:15] toolbox I'm gonna work through kind of
[00:10:17] some stuff with the new yorks data that
[00:10:21] we just collected yes sir not the data
[00:10:23] we collected yesterday but that Thomas
[00:10:25] gave me related to the data we collected
[00:10:27] yesterday this a little bit earlier but
[00:10:29] these you want to follow along you can
[00:10:43] try I'll go through I'm gonna go through
[00:10:48] its like that the new Rex data first
[00:10:51] kind of flake and I'll walk you through
[00:10:53] that but you use these demos you can
[00:10:56] look on at your leisure
[00:10:59] they're really eat actually I can open
[00:11:01] up one there there
[00:11:05] they're really extensively documented so
[00:11:10] like this one
[00:11:10] here's analysis demo if I just hit run
[00:11:12] it'll just run through the whole thing
[00:11:14] but it actually starts off it downloads
[00:11:17] data from bitbucket so it if you don't
[00:11:20] have the data on your computer ill
[00:11:21] actually download it automatically and
[00:11:23] then it walks through loading up the
[00:11:28] data doing basic analysis converting it
[00:11:31] to hemoglobin and doing stats on it and
[00:11:33] stuff I'll talk to you I'll show you in
[00:11:36] a second the way that the data works is
[00:11:40] or the load works is the toolbox is able
[00:11:44] to handle demographic information as
[00:11:47] well so when we get to the level of
[00:11:49] group group level stats and you have a
[00:11:51] study with young and old subjects and
[00:11:55] maybe multiple visits per subject you
[00:11:57] can actually when you run your ANOVA
[00:12:00] testing and stuff you can actually use
[00:12:02] those as covariance in the toolbox and
[00:12:06] this is all set up when you first load
[00:12:09] the data that you have let's say my
[00:12:13] study folder and inside of my study
[00:12:15] folder you can have Group one and group
[00:12:17] two or old and young men whatever and
[00:12:20] then inside of Group one maybe I have
[00:12:22] two subjects a and B as subfolders and
[00:12:26] then inside the list of folders overall
[00:12:27] yamir xscape and so you can specify this
[00:12:33] hierarchy of folder structures and then
[00:12:37] when you load the data you can say well
[00:12:39] the first level denoted the group the
[00:12:40] second level denoted the subject or the
[00:12:43] first level is group the second level is
[00:12:45] the subject the third level is a session
[00:12:47] and so by creating this hierarchical
[00:12:49] folder all I do is I point to this you
[00:12:53] know where's the root folder there
[00:12:54] where's the data live and tell it how to
[00:12:57] interpret the folders and it
[00:12:58] automatically load and populate all
[00:13:00] that's that stuff I'll show you
[00:13:03] I won't show you here but in the example
[00:13:05] there's ways to then load that up from
[00:13:09] Excel or SPSS as well so you can add
[00:13:11] even more information that you can then
[00:13:14] use in your analysis
[00:13:17] it turn to this okay so let me yes so
[00:13:32] you can upload additional demographics
[00:13:34] from an excel file or a or CSV or you
[00:13:40] know I actually load dot save files from
[00:13:42] from SPSS don't tell the SPSS people but
[00:13:46] I hacked their data format because it
[00:13:48] did technically is proprietary yeah but
[00:13:53] it would directly reads dot save files
[00:13:56] yeah don't put that on YouTube oh I I
[00:14:03] totally forgot that this was being
[00:14:05] YouTubed yeah okay okay so I have some
[00:14:12] data the data that you guys also had
[00:14:15] that pomace sent the link to and it's in
[00:14:17] right now I have it in this folder
[00:14:19] called near X demo I have one subject
[00:14:24] I'm sorry that's so I have I've in that
[00:14:29] in that
[00:14:30] Urich's demo folder I've created a
[00:14:32] folder for subject one and if we look
[00:14:35] inside subject one that's the the file
[00:14:39] that that Thomas sent so this is scan
[00:14:42] number two from this subject if I had
[00:14:44] another scan I'd have another scan
[00:14:46] folder and inside of these is your
[00:14:49] typical New York's structures okay so
[00:14:52] each it for neurotics data each scan
[00:14:56] goes into a separate folder
[00:14:58] you know when the narak system collects
[00:15:00] it creates a new folder scan to and
[00:15:02] dumps all the data in there with some of
[00:15:05] the other systems arnis the takun
[00:15:07] systems you're gonna have just a single
[00:15:09] file so you might have a folder with all
[00:15:11] five scans in that file the same thing
[00:15:15] the same thing as true I just have I
[00:15:17] have a subject and inside of that
[00:15:18] subject I have I have all my scans ok so
[00:15:21] what we're gonna do is we're gonna load
[00:15:25] up that data real quick and so I told it
[00:15:30] man's all look something like this so
[00:15:33] the nearest toolbox for the computer
[00:15:38] program that's in the grub it defines
[00:15:40] what's called the main space but it
[00:15:43] basically all commands are something
[00:15:45] like mirrors dot IO for input/output dot
[00:15:48] load directory or nearest I o dot load
[00:15:52] new rocks or nearest math do something
[00:15:55] interesting okay and and so so I called
[00:15:58] it man load directory and telling it
[00:16:00] this Rhode Island folder that contains
[00:16:02] my data it's still busy because I meant
[00:16:08] to I forgot that I changed the folder
[00:16:12] name sorry let me do that again ok I had
[00:16:26] lots of data in that folder so I was
[00:16:28] actually trying to load more than just
[00:16:29] just that but so I told it load the
[00:16:35] directory I told it which folder and I
[00:16:37] told it you're going to encounter this
[00:16:38] hierarchy hierarchy of folders denoting
[00:16:42] subject now it's only going to get one
[00:16:43] subject out of here oh is it still
[00:16:48] this is embarrassing my computer's been
[00:16:52] slow
[00:17:03] fortunately I already loaded the data
[00:17:04] this morning so we're gonna just stop
[00:17:06] there I think that's well I'll pretend
[00:17:10] like that didn't happen okay it does
[00:17:12] work I swear my computer's just doing a
[00:17:15] lot of stuff right now anyway so we
[00:17:18] loaded up the data via that raw that
[00:17:21] load data load directory function if I
[00:17:24] had lots of subjects or something it
[00:17:26] might take a little bit of time to load
[00:17:28] it's actually loading you kind of
[00:17:32] started a little bit when it loaded it
[00:17:34] said it was loading the head mash which
[00:17:36] is this 3d registration from the near
[00:17:38] acts it only does it for the first
[00:17:40] subject and then just copies it all for
[00:17:42] there all the other subjects but there's
[00:17:43] a way if you for some reason did have a
[00:17:46] different montage for every subject it
[00:17:47] will load it that way most the time
[00:17:50] spent loading is loading that montage so
[00:17:53] I only really want to do it once and
[00:17:55] once I have to but what gets loaded is a
[00:18:00] this data variable I called it raw and
[00:18:03] it's actually a structure containing the
[00:18:07] information about where the data came
[00:18:09] from so description the actual data
[00:18:12] itself which is 1800 time points by 40
[00:18:14] channels the probe which describes where
[00:18:18] those 40 channels came from and I'll
[00:18:20] show that in a second information about
[00:18:23] the stimulus timing information about
[00:18:25] demographics and the sample rate and
[00:18:27] this is actually what's what's called a
[00:18:30] MATLAB object or class class definition
[00:18:34] and it's it's actually what's what's
[00:18:37] nice about this is that raw the object
[00:18:42] knows how to draw itself so I have these
[00:18:47] what are called methods and the the
[00:18:50] methods will come on please work
[00:18:54] computers slow ok there so I drew a
[00:18:57] channel 1 from raw and you see that's
[00:18:59] that's the data is time chorus you see
[00:19:02] the scheme this information put on so
[00:19:04] these these objects have methods that I
[00:19:08] can I can call like draw and depending
[00:19:11] on what the object is whether it's raw
[00:19:15] data or
[00:19:15] hemoglobin or a stats variable when I
[00:19:18] say draw it automatically knows what
[00:19:21] that means and so it's a let's go
[00:19:23] context specific function it knows that
[00:19:26] if I'm a a stats object and you said
[00:19:29] draw do it this way if I'm a raw data
[00:19:31] core time course like this do it this
[00:19:33] other way yeah yeah I'll show you that
[00:19:45] we're getting over this is this is just
[00:19:47] the the start of this and I realized I
[00:19:50] only have 20 minutes but we'll keep
[00:19:53] going okay so so so there is so so we do
[00:19:59] have a number of pulses let me quickly
[00:20:03] sit back so right now there's only one
[00:20:04] data file and in loaded one if I had
[00:20:07] multiple subjects whatever this would
[00:20:09] actually be what's called an array it
[00:20:11] would have multiple entries so I would
[00:20:12] say raw one dot draw or raw to draw if I
[00:20:15] said rod at draw and I had ten subject
[00:20:18] he would actually draw all ten images
[00:20:20] like like that we have a number of tools
[00:20:24] in here and again all of this is in that
[00:20:26] so don't jot down too many notes because
[00:20:29] it's all in the demos but there is a
[00:20:32] number of graphical interfaces that
[00:20:36] really sorry so I think that's
[00:20:43] embarrassing that's really embarrassing
[00:20:55] this is because I was playing around
[00:20:57] with it this morning trying to do stuff
[00:20:59] that I shouldn't have done ends
[00:21:02] [Music]
[00:21:24] I cannot type under pressure okay sorry
[00:21:31] what it was doing I had created a
[00:21:33] variable that it didn't want to load
[00:21:36] because it was done this is money and
[00:21:39] it's still fortunately I have a
[00:21:52] PowerPoint first class so I switch to
[00:21:55] that I'll come back to that it's just
[00:21:59] this one program that's not working
[00:22:00] properly
[00:22:02] [Music]
[00:22:19] I'm sorry I will fix this this is you
[00:22:23] know I said at the very beginning if I
[00:22:25] encounter a bug as I'm going through
[00:22:26] this I will fix it before I even land in
[00:22:28] Pittsburgh I don't know why this is not
[00:22:31] happy right now I'll switch over to a
[00:22:38] different version this one but there's
[00:22:45] there's a number of these kind of gooeys
[00:22:47] these graphical interfaces that lets you
[00:22:51] navigate through your data so if you
[00:22:54] want to visualize what my data actually
[00:22:56] looked like so if I had multiple
[00:22:58] subjects he would have a big long list I
[00:23:00] would select which file it was showed me
[00:23:02] the time horse now I understand it'll
[00:23:12] display here the problem oh I'm gonna
[00:23:34] stop embarrassing myself at this point
[00:23:36] anyway so there's a number of these
[00:23:38] these these graphical interfaces that
[00:23:42] that you can visualize the data but most
[00:23:45] of the analysis is actually done kind of
[00:23:47] from the command line
[00:23:48] okay so we've loaded up the raw data we
[00:23:52] have the steeled data that actually
[00:23:54] describes the data we have this field
[00:23:56] probe that describes the the probe
[00:23:58] geometry I'm gonna show that right now
[00:24:00] we have this field stimulus that defines
[00:24:03] the different events and their duration
[00:24:05] and amplitude and so on if we look at
[00:24:08] the raw probe so it contains information
[00:24:12] about not only the like the source
[00:24:17] detector positions but it also because
[00:24:22] this is near acts data and Thomas
[00:24:24] registered it up on to the head it
[00:24:26] actually has all their information about
[00:24:27] 10-20 as well and so what I can do
[00:24:31] and kind of saw it a little bit is I can
[00:24:33] actually draw that probe then in like a
[00:24:38] 1020 map or you saw it as a 3d map this
[00:24:41] is the problem that's causing with my
[00:24:42] data is this old this the data Thomas
[00:24:45] gave me your ex has changed something
[00:24:48] with their data format and so my
[00:24:50] registrations are not interpreting it
[00:24:53] right and hence my motor cortex is
[00:24:56] apparently too too small and too far
[00:24:58] forward and that's what's causing the
[00:24:59] issues right here and I'm gonna fix it
[00:25:01] just give me a plane right on the
[00:25:03] Pittsburgh but you have these fees
[00:25:06] because the probe has been registered we
[00:25:08] can actually view this in the 10 20 maps
[00:25:11] like this we can also view it sitting on
[00:25:14] the brain now I'll show you more of that
[00:25:17] as we keep going ok so the first thing
[00:25:26] we want to do if we look at this task we
[00:25:32] know that so this is just the stimulus
[00:25:34] time so this was 281 seconds long
[00:25:37] through these two events channel 1 and
[00:25:41] channel 15 which Ben Thomas collected
[00:25:43] the data was tapping your right hand and
[00:25:47] left hand respectively or other way
[00:25:49] around it left hand right hand okay and
[00:25:51] we know we did it for 10 seconds long ok
[00:25:55] so I said kind of early and like my
[00:25:57] first talk if we want to do the
[00:25:59] parametric modeling the kind of the
[00:26:01] canonical model we need to actually know
[00:26:03] not only when the events occurred that
[00:26:05] how long they were so one of the first
[00:26:09] depending on how you collect the data so
[00:26:12] in my systems we have say e prime
[00:26:15] sending a signal on for the whole
[00:26:18] duration the whole 10 seconds and then
[00:26:19] off and I just I I know from that what
[00:26:22] the duration is in this case we only
[00:26:24] have a mark at the beginning so we have
[00:26:26] to go in and enter that information sort
[00:26:28] of manually it depends on how your data
[00:26:32] was set up so what we can do is we can I
[00:26:35] wrote this utility last night or on the
[00:26:39] plane yesterday
[00:26:42] it works what it is is it's the that
[00:26:55] whatever that stream screen capture
[00:26:57] software this is completely slowing down
[00:27:00] my computer it's it's it's okay but I
[00:27:06] wrote this it's it's called skim utility
[00:27:08] and so I loaded up this data you see
[00:27:12] that channel information of channel 1
[00:27:14] had four events at twenty three seventy
[00:27:18] three hundred seconds the other ones so
[00:27:23] let's go and let's rename them real
[00:27:24] quick so channel one right-click rename
[00:27:27] and that was left and if we right-click
[00:27:35] on here we can set all the durations we
[00:27:38] know they were ten seconds long okay
[00:27:43] you're the same thing for channel 15
[00:27:45] we're gonna rename it to right and we're
[00:27:53] again gonna set all the durations to ten
[00:27:56] seconds well that's updating so what's
[00:28:04] nice about the Encinal fights that rada
[00:28:06] draw it'll actually draw with that
[00:28:09] ten-second duration so now when I
[00:28:11] develop my model of what parts the brain
[00:28:13] looked like this timing it knows about
[00:28:16] the duration if I had if I had as I said
[00:28:20] earlier like a self-paced experiment
[00:28:22] where the duration is different for each
[00:28:24] each block we can model that there was
[00:28:28] also a field called amplitude amplitude
[00:28:30] is used to familiar with fMRI design in
[00:28:33] parametric models where I can basically
[00:28:36] have each block amp module moderated by
[00:28:42] some other factor like reaction time or
[00:28:45] something like that and what I can do
[00:28:47] then is then I have when I set up my
[00:28:49] model I can ask the hypothesis of which
[00:28:52] channels which channels should brain
[00:28:55] active
[00:28:56] that changed related to reaction time
[00:28:59] right so you have let's say some some
[00:29:04] set of channels that activate from the
[00:29:06] task and some subset of those that were
[00:29:09] responding selectively to reaction time
[00:29:12] maybe these parts of my brain just
[00:29:14] reacts to the task but only this part of
[00:29:17] my brain is actually changing what I've
[00:29:19] become faster at the task that's an fMRI
[00:29:21] what's called a parametric design my
[00:29:24] toolbox can handle that
[00:29:25] if you put in amplitude information it
[00:29:28] can handle both linear and nonlinear
[00:29:30] versions of that which is which is
[00:29:33] getting into it gives you the ability to
[00:29:36] do exactly the same statistics that you
[00:29:40] do and your people my colleagues are
[00:29:42] familiar with doing with fMRI and
[00:29:44] they've demanded that they also should
[00:29:47] be able to do with nerves so anyway so
[00:29:49] we have we have the data loaded right
[00:29:51] now because as I said because this is
[00:29:56] near acts data it has that information
[00:29:59] about the probe design and the
[00:30:03] registration and so this command probe
[00:30:08] default draw function that controls the
[00:30:11] default draw function it defines when I
[00:30:14] issue that draw command how it's going
[00:30:16] to interpret it and so the default is a
[00:30:19] two dimensional probe if I say question
[00:30:22] mark it prints out all the different
[00:30:24] options and so you see there's different
[00:30:27] options there's ten twenty ten twenty
[00:30:29] zoom where it's only going to zoom in
[00:30:31] the region that I have to probe its so
[00:30:33] put it in ten twenty space we can also
[00:30:35] do 3d meshes where a winner go to raw
[00:30:37] that brain and we're gonna draw the
[00:30:39] probe overlaid so we're gonna change
[00:30:41] this actually will change it to 3d mash
[00:30:45] showing it from the superior direction
[00:30:48] and so now if I say draw it should
[00:30:54] actually draw a picture of the brain
[00:30:57] there we go and this is actually an
[00:31:00] object that we can rotate around and so
[00:31:04] on again I apologize because the probe
[00:31:07] is clearly miss registered a little bit
[00:31:10] but I will fix that anyway so there's
[00:31:13] that we're gonna change it back to this
[00:31:17] just sort of run so faster also knowing
[00:31:20] the registration what I can do I have
[00:31:23] these utility functions
[00:31:26] this one's called depth map and I'm
[00:31:29] sorry I'll bring that up higher on the
[00:31:30] screen in a second as soon as it
[00:31:32] finishes but depth map I mean what I did
[00:31:36] is I said depth map and I said I want to
[00:31:40] look at the precentral sulcus and I want
[00:31:43] you to overlay where my probe was
[00:31:45] relative to that and so it comes up with
[00:31:48] this map is based on the column 27
[00:31:52] depending States but this is depth from
[00:31:55] the surface of the scalp so this tells
[00:31:58] me that all the regions in yellow are
[00:32:00] greater than 30 centimeters you know
[00:32:02] prefrontal cortex or like pls central
[00:32:05] gyrus with more than 30 centimeters away
[00:32:07] from the back your head what if these
[00:32:11] regions if I have my curve right here in
[00:32:13] these company space I'm kind of in that
[00:32:15] ballpark 15 to 20 millimeters which is
[00:32:18] accessible by nears you can also see I
[00:32:21] kind of mix register to create this too
[00:32:23] far forward okay okay
[00:32:32] so so you can look at the data you can
[00:32:36] change your stimulus information you can
[00:32:39] add demographics and so on and that all
[00:32:42] gets walked through in the demo or
[00:32:44] there's those example scripts when
[00:32:46] you're ready to actually run analysis
[00:32:50] there's the processing pipe and so what
[00:32:58] you do is you create a pipeline by
[00:33:01] basically stacking these modules
[00:33:03] together so this this set of four lines
[00:33:06] what it's going to do is he's going to
[00:33:08] calculate octave events it's gonna take
[00:33:10] my raw data turn it to optical density
[00:33:12] it's been a resample that resample
[00:33:14] function had options that default is for
[00:33:16] earths
[00:33:17] and then it's gonna run the bear
[00:33:19] elaborately it's
[00:33:21] so I created that pipeline with these
[00:33:23] three jobs and then I ran that job on
[00:33:27] the raw data saving the result is
[00:33:29] another so now when I go and finished
[00:33:32] and I say hemoglobin spell it right draw
[00:33:37] and I want to show that same first
[00:33:40] channel now instead of when I said
[00:33:43] Roddick draw is drawing the raw data
[00:33:45] now when I say hemoglobin net draw it's
[00:33:47] actually drawing eliminated so this
[00:33:49] happens to be the oxyhemoglobin for the
[00:33:51] first channel and you see my experience
[00:33:54] events and so on like that okay so so
[00:34:13] okay so there's a series modules for
[00:34:19] basic pre-processing no conversion to
[00:34:21] optical density here Lambert there are
[00:34:26] as I said we don't really do it very
[00:34:29] much
[00:34:29] all that PCA and motion correction is in
[00:34:32] there although it's not my default
[00:34:33] pipeline because although it's useful to
[00:34:36] be in there so you can compare it what
[00:34:38] does it look like if I processed this
[00:34:40] way the old-school way versus the
[00:34:42] new-school way bad terminology but but
[00:34:46] you can go and you can compare the
[00:34:48] different approaches and they are in the
[00:34:49] toolbox my preference is kind of not to
[00:34:52] do that so what I'm running right now is
[00:34:55] I ran my module called GLM
[00:35:09] this data doesn't happen here at near
[00:35:12] distances this was basically what we
[00:35:14] collected yesterday with Thomas which is
[00:35:16] you know three centimeter sources the
[00:35:18] factor of distances on the left and
[00:35:20] right motor cortex note short distances
[00:35:22] so so the way that and this is like ten
[00:35:28] publications being expressed in like two
[00:35:31] sentences the way that it turns out that
[00:35:36] noise physiology motion etc is bad for
[00:35:42] two reasons one noise is just bad if you
[00:35:46] have less noise you have better data in
[00:35:47] the other two seats smaller effects to
[00:35:51] noise every time you do a statistical
[00:35:54] model you make certain assumptions so
[00:35:57] you run a general in your model you're
[00:35:58] assuming the data is normally
[00:36:00] distributed stationary I said that it's
[00:36:03] uncorrelated and the problem is our data
[00:36:06] is not a beta has outliers for there's
[00:36:10] no chart effects it has slow drift
[00:36:12] because it has all that physiology which
[00:36:15] means that the statistical model like
[00:36:18] the face the basic statistical model is
[00:36:21] actually wrong whether this means your
[00:36:22] data
[00:36:23] it's these assumptions and those
[00:36:26] assumptions are violated so the solution
[00:36:29] is two solutions one either go to your
[00:36:31] data and pre-process it to remove those
[00:36:33] the problems or to change your
[00:36:37] statistical model and choose one that is
[00:36:39] less sensitive to those assumptions
[00:36:41] that's different set of assumptions I
[00:36:43] tend to prefer the second so what we've
[00:36:46] been doing so so while it's still true
[00:36:49] that if I preprocessor and I removed the
[00:36:51] Moshe artifact that have less noise and
[00:36:53] I maybe be happier by choosing a
[00:36:56] statistical model that really didn't
[00:36:57] care about motion artifact and it was
[00:36:59] able to handle a heavy tailed outlier
[00:37:02] it's and serial correlations and so on I
[00:37:04] can actually not even have to do that
[00:37:07] pre-processing and still get a
[00:37:15] yes yes so might the GLM model know if I
[00:37:21] can bring this ring up a little bit to
[00:37:24] show okay so so the as I'm sorry because
[00:37:28] I know the podium is blocking this so
[00:37:30] this GLM module has a number of
[00:37:34] different options some of the other ones
[00:37:37] like the resample had options charities
[00:37:38] didn't show up but when you load and
[00:37:40] create the job it's a structure that
[00:37:43] contains a number of things that you can
[00:37:44] change so one of the things you can
[00:37:46] change is what type of GLM bottle
[00:37:48] do you wanna use and the default here as
[00:37:51] you point out is the auto regressive
[00:37:53] iterative recursively sweater it's I
[00:37:57] forget what that acronym is something
[00:37:59] it's the barker at all two thousand
[00:38:01] thirteen or fourteen method and it's
[00:38:04] like that's the way that I strongly
[00:38:06] recommend to analyze your day it was the
[00:38:08] ninety percent of the math in my talk
[00:38:11] that I didn't get this afternoon the way
[00:38:14] that this algorithm works is there's
[00:38:17] again there's two problems with with the
[00:38:19] nearest data there is physiology slow
[00:38:21] drips and you over sampling which means
[00:38:24] that is what's called serially
[00:38:26] correlated error so it means that you
[00:38:28] might have a thousand when the space
[00:38:30] between whatever 100 data points but you
[00:38:34] don't have that number of degrees of
[00:38:35] freedom you know far less because your
[00:38:38] measurements were not independent right
[00:38:40] and that's what's called serial
[00:38:41] correlations and so so what they
[00:38:45] approach them to take the serial
[00:38:46] correlations use we pick the model once
[00:38:49] take the residual design a filter that's
[00:38:52] going to whiten that research now that
[00:38:54] means it's no longer going to violate
[00:38:56] our assumptions and we go back and we
[00:38:59] apply that filter to both sides of the
[00:39:02] equations both to the design matrix and
[00:39:04] to the data itself and then when we
[00:39:06] solve it again
[00:39:07] now we've we're no longer violating our
[00:39:10] assumptions on our scatter actually
[00:39:13] we're also doing what's called weighted
[00:39:16] least squares which deals with the
[00:39:19] second problem in the nearest data that
[00:39:21] we often have motion effects this data I
[00:39:23] don't think add
[00:39:25] any motion artifacts but if you deal
[00:39:26] with kids I guarantee your data does and
[00:39:28] those artifacts right we saw the data
[00:39:31] cruising along and then suddenly jumps
[00:39:32] off and I come in and step down and they
[00:39:35] be shifted and so on but that those kind
[00:39:38] points where it jumped up come back down
[00:39:39] were so much higher noise than the rest
[00:39:42] of the base the rest of the game right
[00:39:44] there are outliers and so he can do
[00:39:47] statistical methods with bus regression
[00:39:50] specifically that deals with outliers
[00:39:52] and so now that's a statistical model
[00:39:55] that is less sensitive having outliers
[00:39:58] in the data and so especially if you
[00:40:02] autoregressive good filter those
[00:40:04] artifacts just appearance like there was
[00:40:06] one point in time you just have so much
[00:40:08] more noise to both ships and spikes
[00:40:11] likes artifacts and so by dealing with
[00:40:14] these were bus stats now I still have
[00:40:18] the noise in the data but didn't have
[00:40:19] the noise in the data might be school
[00:40:21] sports could be higher but because I've
[00:40:24] chosen the rights is a model I teach
[00:40:26] scores are correct and I if you brought
[00:40:29] out like false discovery rate and stuff
[00:40:31] you have no uncontrolled type on error
[00:40:33] and so on we spent a lot of time getting
[00:40:37] that right if you don't do that and
[00:40:40] again I don't want to knock anyone who's
[00:40:43] currently doing gears research but
[00:40:45] you're doing say Homer code which
[00:40:47] doesn't account for this kind of stuff
[00:40:49] Homer can tell you say Oh show me the
[00:40:52] results at 0.05 stats it's closer to me
[00:40:55] depending on how bad your data is but it
[00:40:58] can be 60 to 80 percent false discovery
[00:41:00] which means that you're reporting on
[00:41:04] results that probably work and it's it's
[00:41:08] because you violated because the
[00:41:10] statistical test you did was not valid
[00:41:12] for that kind of data so that's that's
[00:41:18] that's what we work yeah
[00:41:34] so what you do okay so by equals x times
[00:41:39] beta right that's your your linear
[00:41:41] regression solve the model once take the
[00:41:44] residual take the residual and find fit
[00:41:47] it to an autoregressive model let's
[00:41:49] let's call that app then go back and say
[00:41:53] F times y equals F times x times beta
[00:41:56] and solve again for beta and you keep
[00:41:59] iterating on that
[00:42:08] no no no it's it's it's it's a it's a
[00:42:12] finding the optimal filter from the from
[00:42:16] the residual and then applying that
[00:42:17] filter to both sides of the equation and
[00:42:19] then keep going and it's the same thing
[00:42:21] with the weeding through the squares
[00:42:23] when you do the residual you calculate
[00:42:25] the probability of being an outlier so
[00:42:27] these motion artifacts get down weighted
[00:42:38] no it's the residual is a time course
[00:42:41] still it's it's yeah it's I can I can
[00:42:46] work through the nap a little bit more
[00:42:48] writing equations in the air that only I
[00:42:50] can see is it's not going to suicides
[00:42:55] yeah
[00:43:08] yeah it it yeah it's it's um it's
[00:43:17] continue to time series analysis yeah
[00:43:19] it's it's it if there's other ways to
[00:43:21] kind of do the black it's it's it's when
[00:43:25] you doing regression your noise is
[00:43:27] estimated from the residual everything
[00:43:30] that wasn't part of the bottom we need
[00:43:31] to a block average your noise it's
[00:43:34] estimated for each time point
[00:43:36] individually and so it's a little bit
[00:43:38] it's a little bit different it still
[00:43:42] does have these problems it's not yeah
[00:43:53] yeah
[00:43:54] if you compressed it first and then yeah
[00:43:57] it's yeah that is true
[00:44:05] yeah there are there are other
[00:44:07] approaches to this this is certainly not
[00:44:10] the only solution there are there are
[00:44:13] yeah yeah no no no no it's it's in and I
[00:44:16] always I always kind of hesitate when
[00:44:19] it's like oh you're data's bad and
[00:44:21] someone like like gives up doing mirrors
[00:44:24] because they walked out of my lecture or
[00:44:25] whatever and like please don't it's what
[00:44:27] you did was probably not that bad but
[00:44:29] moving ahead that's do it right yeah so
[00:44:33] so so I'll show in a second to there's a
[00:44:36] field here called basis set where you
[00:44:38] can actually set what basis set you're
[00:44:40] gonna use a show this can be my default
[00:44:43] with the canonical model but we can also
[00:44:45] do the deconvolution in this as well
[00:44:48] there's trendy regressors if you want to
[00:44:50] put in polynomials or something to
[00:44:52] remove drift and so on but what came out
[00:44:56] of that is when I call it subjects cats
[00:45:01] and so it is you'd the job you know job
[00:45:05] dot run of vet in hemoglobin so what
[00:45:08] came back out was a slightly different
[00:45:10] class called channel stats channel stats
[00:45:14] just like the data knows how to draw
[00:45:16] itself it has features containing the
[00:45:20] description
[00:45:21] any of the demographics the same probe
[00:45:23] variable but now instead of holding the
[00:45:25] data as a time chorus it's actually
[00:45:27] holding the estimates of your regression
[00:45:29] model the noise of your regression model
[00:45:32] the t-score the Peace Corps and the Ben
[00:45:36] jihadi Hochberg
[00:45:37] FDR corrected Q value which is the false
[00:45:41] discovery rate so you can issue a
[00:45:43] commands like I said it knows how to
[00:45:47] draw itself and and I can I can just say
[00:45:49] dot draw and it knows what that means
[00:45:54] because it's it carried through that
[00:45:57] probe it should actually be the three
[00:45:59] dimensional not a two-dimensional
[00:46:00] version because it looked at that
[00:46:03] default draw function I had set it to be
[00:46:05] 2d and so it knows how to draw right
[00:46:07] here it's showing the opsin going to go
[00:46:09] down the right sides and you get
[00:46:11] left-sided activity left-sided activity
[00:46:16] that's oxy on the right here's the
[00:46:18] oxidant left I'll just close these guys
[00:46:20] ok so there's there's my left and the
[00:46:22] right finger tapping so it went to the
[00:46:25] right side right this is the East score
[00:46:29] by default but what you can do is you
[00:46:34] can we can change that with defaults and
[00:46:39] let's change that to the 3d mesh and now
[00:46:49] if I you should I draw a command and I'm
[00:46:51] gonna give it some other options that I
[00:46:53] I'm gonna explicitly tell it I want to
[00:46:55] show tc-stats I want to auto scale it
[00:46:59] and I want to show Q less than 0.05 so
[00:47:02] now it's only gonna draw solid lines he
[00:47:06] if it met that FDR corrected statistical
[00:47:09] threshold which hopefully the data did
[00:47:12] because I didn't actually look at this
[00:47:13] but we saw it there and this is N equals
[00:47:16] one with four trials I wouldn't be
[00:47:19] surprised if it didn't survive stats yet
[00:47:22] [Music]
[00:47:24] get drunk up there yeah they're just
[00:47:30] slow
[00:47:31] but now you see I changed the default
[00:47:35] draw function so now it's drawing it in
[00:47:39] that 3d mode okay
[00:47:41] and actually you see that the only
[00:47:44] things that survived when I cut my right
[00:47:46] hand at Kiva love Oh 5 is the left side
[00:47:50] and the only thing that survived was my
[00:47:52] left hand with the right side you lunge
[00:47:55] down over there so all of that kind of
[00:47:58] background survived my statistical
[00:48:01] testing
[00:48:06] yes it's correcting for it's actually
[00:48:10] correcting for anything within the
[00:48:12] variable so right now the variable this
[00:48:16] this channel stats variables it contains
[00:48:21] both oxy and the oxy for all 30 some
[00:48:24] channels of data at both conditions left
[00:48:27] and right so I'm actually correcting for
[00:48:30] that whole 80 degrees of freedom you
[00:48:33] know 80 different tests that are being
[00:48:35] performed with it with the Ben Johnny
[00:48:37] Hochberg I can also do if I if I wanted
[00:48:41] to test so one of the other like draw a
[00:48:46] stats variable that's how to do a t-test
[00:49:04] here yes
[00:49:06] so the that stats variable that
[00:49:10] covariance matrix is full its storing
[00:49:13] channel by channel oxy by oxy the whole
[00:49:16] covariance matrix so so yes they are not
[00:49:21] independent dependent measures when I'm
[00:49:24] drawing these images like this I'm doing
[00:49:30] I'm basically taking only the diagonal
[00:49:32] part of that covariance matrix that may
[00:49:34] be passed on this channel on this
[00:49:36] channel which is why I have to FDR
[00:49:37] correct it but when we go to region of
[00:49:41] interest or image reconstruction
[00:49:44] I can actually make use of oxy and EOCs
[00:49:46] are not actually independent measures
[00:49:47] and I have that information available to
[00:49:49] you so we do account for the fact that
[00:49:51] these five channels the noise might have
[00:49:54] been correlated when we do like a region
[00:49:56] of interest average which I'm going to
[00:49:57] show you in a second but yeah it's it's
[00:50:01] it's right now I'm storing all the
[00:50:03] information for oxy deoxy I'm not really
[00:50:06] doing anything with it yeah it's using
[00:50:18] right now it's using the same basis set
[00:50:20] for both oxy and biopsy it's not using
[00:50:23] the live version as I said if the task
[00:50:25] is longer than about 10 seconds it
[00:50:27] doesn't but those are open questions
[00:50:36] yeah there is yeah and actually with um
[00:50:40] I'll go back and show it in that Jeff
[00:50:42] GLM module there was a field called
[00:50:46] basis and I'll just show it right now so
[00:50:53] job dot basis it has so so so it has a
[00:51:05] default basis set and so this is the
[00:51:09] canonical model that it's going to use I
[00:51:10] can change this and reassign it if I
[00:51:13] said defaults : oxy and default colon
[00:51:17] deoxy I can actually have a different
[00:51:19] basis set for the two components in the
[00:51:21] model I can also have a different basis
[00:51:23] set for left versus right if for some
[00:51:25] reason I had a reasonably if the left
[00:51:28] timing was gonna be different from the
[00:51:30] right time I'm gonna actually do it you
[00:51:32] can put in derivatives if you put in
[00:51:35] derivatives to your canonical model it
[00:51:36] can model shifts in the data so there
[00:51:40] are there is a huge amount of
[00:51:42] flexibility to model this anything you
[00:51:45] can do in SPM we can do here but it's
[00:51:49] not advanced topics for this discussion
[00:51:56] but what oh I'm totally yeah yeah okay i
[00:52:10] i'm rep yeah i yeah i'm not insulted i i
[00:52:27] i will try to wrap this this this this
[00:52:29] up this is good conversation though but
[00:52:34] you can okay so as I said there are
[00:52:36] methods that the object know certain
[00:52:40] keywords like draw and we saw how it
[00:52:42] draw drew itself I can all see keywords
[00:52:45] like t-test and so I can say t-test give
[00:52:48] me the key test of left versus right
[00:52:50] there right versus left right and then I
[00:52:54] decided to draw that and so this is the
[00:52:56] image of the brain activity of
[00:52:59] oxyhemoglobin of the right condition -
[00:53:01] the left condition in this case doesn't
[00:53:04] really make sense one it's gonna be red
[00:53:06] ones blue pigs
[00:53:07] it was greater in left and right over
[00:53:10] here and it's breather and right and
[00:53:12] left you get the idea right if I had
[00:53:15] done something like I'm back to vs. n
[00:53:18] back bond it might have been a little
[00:53:19] bit more meaningful because it's in the
[00:53:21] same area but what you can actually do
[00:53:25] all the T tests to compare different
[00:53:27] conditions and so on within the code it
[00:53:33] can handle one this maybe this might
[00:53:40] take a little bit of time with my
[00:53:41] computer being slow but if I change that
[00:53:43] basis set the default was the canonical
[00:53:45] I can use a deconvolution model and now
[00:53:49] when I used to that same command to run
[00:53:52] the GLM model it's going to actually do
[00:53:55] a deconvolution and so now instead of a
[00:53:57] assumed shape I'm gonna actually have a
[00:53:59] whole time course and I could run so I
[00:54:02] can take a look at that
[00:54:07] this in the sake of time you're just
[00:54:12] gonna have to trust me that that that
[00:54:14] works I might pull up the image in a
[00:54:16] second but it's my computer is being
[00:54:18] really slow cuz I'm learning the screen
[00:54:20] capture software on it right now and
[00:54:22] it's driving me nuts and I'm very
[00:54:23] impatient but once you get that then as
[00:54:28] I said if we had the human response the
[00:54:33] whole time course it's a two-step
[00:54:34] process you have that and then you have
[00:54:36] to define a window so this command here
[00:54:40] I'm gonna run a few tests I'm gonna use
[00:54:42] the block from 8.2 the 24 point this is
[00:54:47] at 4 Hertz so this is actually 2 seconds
[00:54:50] - and actually if I do that it's gonna
[00:55:00] look very similar to the activity map
[00:55:02] that I showed before it was the
[00:55:03] canonical if I had actually instead of
[00:55:06] just taking straight out to the 6
[00:55:08] seconds I had done a tapered window
[00:55:10] I've given kind of a weight that's going
[00:55:13] up and keeping that at 6 seconds I would
[00:55:16] have gotten actually the exact same
[00:55:17] stats as the other model and what you
[00:55:21] can do subjects that's got table if you
[00:55:27] say table with another keyword it'll
[00:55:29] actually spit out all of this
[00:55:31] information about beta and degrees of
[00:55:32] freedom and so on you can copy paste
[00:55:35] that into Excel or SPSS or whatever you
[00:55:43] can do it's a highlight the other thing
[00:55:55] again all of this is in these demos so
[00:55:58] I'm just I'm kind of quickly going
[00:56:00] through here but we can also define
[00:56:04] regions of interest so in this case this
[00:56:07] region of interest that there's a number
[00:56:09] of different ways you can specify it but
[00:56:12] you basically tell me the source and
[00:56:13] detectors and you can use not a number
[00:56:16] or n a n as kind of wild card so so this
[00:56:20] is
[00:56:21] orcid is one two three and four which
[00:56:23] was the left hemisphere to any detectors
[00:56:26] and sources five six seven and eight to
[00:56:29] any detectors so basically this is the
[00:56:31] left side of the progress of the right
[00:56:32] side of the probe and so if I issue this
[00:56:34] command then RI
[00:56:36] dots utilities dots all right Everage
[00:56:42] given my stats and the ROI definitions
[00:56:52] it'll actually now computes the left
[00:56:55] versus right you know left side of the
[00:56:58] head versus right side of the head
[00:57:00] region of interest for the left tapping
[00:57:02] versus right tapping condition again it
[00:57:05] spits back all of these the the beta
[00:57:08] values their errors the few sports he
[00:57:11] values the two and it'll actually spit
[00:57:14] back a power estimate at the end too
[00:57:16] because I can ask for maybe I can ask me
[00:57:19] given your degrees of freedom and number
[00:57:21] of subjects and stuff I can ask to me
[00:57:22] what your beta was so this is actually
[00:57:24] you know really well powered except for
[00:57:27] that region interest down there
[00:57:29] and one of the things in mirrors that
[00:57:31] I'm starting to appreciate a lot more
[00:57:33] and working to my papers and stuff is
[00:57:36] when you talk about power analysis when
[00:57:38] you do fMRI for the most part all of
[00:57:41] your channels have your voxels have the
[00:57:43] same noise in years that's not
[00:57:46] necessarily true if you had a probe that
[00:57:49] was measuring say from the forehead or
[00:57:51] the side of the head and the occipital
[00:57:53] the power in the occipital is going to
[00:57:55] be much much less because you have more
[00:57:57] noise across the board all your subjects
[00:57:59] going to have much more noise back here
[00:58:01] and so your power estimate out here back
[00:58:04] here is going to be much lower than your
[00:58:05] power s fed up here and therefore if I
[00:58:09] see activity and it was only in the
[00:58:11] forehead I can't really rule out that
[00:58:14] there wasn't activity in the back of
[00:58:16] heaven if I had recorded more subjects
[00:58:18] right so you have to consider that power
[00:58:19] analysis in there and we've started to
[00:58:21] actually put that in in here I will show
[00:58:28] them module
[00:58:33] [Music]
[00:58:35] it will run if I had more subjects and
[00:58:39] more time to explain things this is my
[00:58:41] last note I swear it does do group level
[00:58:46] analysis so what would happen if I had
[00:58:49] multiple files multiple subjects it is
[00:58:52] it would have gone through run that GL a
[00:58:54] model on all the subjects the stats
[00:58:56] variable would have had multiple entries
[00:58:58] one for each subject there once month
[00:59:01] for each file and then I can run this
[00:59:03] module of mixed effects that's gonna do
[00:59:07] a mixed effects group analysis one of
[00:59:10] the fields here is the formula and you
[00:59:14] can specify this is the formula it's
[00:59:16] going to be used for the mixed effects
[00:59:17] model and so this right here the default
[00:59:19] is I'm gonna look at theta ignore the
[00:59:22] intercept
[00:59:23] I'm gonna look for route 5 conditions
[00:59:25] reading subject as a random variable and
[00:59:28] so this is what's called Wilkinsons
[00:59:29] notation it's used it's interpreted by
[00:59:33] SPSS but it's it's the way to specify
[00:59:40] these different formulas and so we can
[00:59:42] specify complicated formulas with with
[00:59:46] quadratic terms and so on random effects
[00:59:49] fixed effects etc and then run our model
[00:59:52] the reason we do it in the code here so
[00:59:56] you could as I said copy-paste to get in
[00:59:58] SPSS and run it in your own way however
[01:00:02] SPSS knows nothing about the covariance
[01:00:06] between oxy and deoxyhemoglobin you know
[01:00:08] there's nothing about the spatial
[01:00:09] covariance that these two channels on my
[01:00:12] head had shared noise terms and so doing
[01:00:16] it here I'm actually doing it in a way
[01:00:18] that controls for that and which is
[01:00:22] something that SPSS can't do SPS you can
[01:00:26] do weighted but you can only deal with
[01:00:27] the diagonal component not the off
[01:00:29] diagonals which is the oxy oxy crosstalk
[01:00:33] pipe curtains and so doing it here in
[01:00:36] principle at least is more is better
[01:00:39] the in practice I've not really seen a
[01:00:42] difference but in principle it's better
[01:00:44] so but we
[01:00:46] support within this any sort of mixed
[01:00:50] effects type models it will do is
[01:00:53] another version that takes the same
[01:00:54] input that does ANOVA there's a quicker
[01:00:57] fixed effects if you don't want to worry
[01:00:59] about the random effects terms that runs
[01:01:01] faster it will output diagnostic
[01:01:06] variables so you could plot like brain
[01:01:08] activity versus subject to look for
[01:01:11] outliers and then you can actually
[01:01:12] remove outliers from your data that way
[01:01:15] you can put me in covariance like
[01:01:18] anything that's in the demographics so
[01:01:22] if I had multiple folders that denoted
[01:01:25] subject or visit or group or whatever I
[01:01:27] can use those as keywords in this
[01:01:29] formula if I input additional
[01:01:32] information like the near X data itself
[01:01:41] when I loaded that data variable when
[01:01:44] you save your Marek's data it went
[01:01:46] through and asked you what is the
[01:01:47] subject ID in and what is their gender
[01:01:49] and age because it's all in the file I
[01:01:52] already have all that information in
[01:01:54] this one happened to you know Thomas
[01:01:57] didn't enter in that information but if
[01:01:58] you did it would all be available and
[01:02:01] because age is a variable I could put in
[01:02:03] that model and I could look at well did
[01:02:05] brain activity change with age with
[01:02:07] gender or whatever so we can deal with
[01:02:09] all of that same stuff you would do in
[01:02:11] SPSS we're just able to do it in in kind
[01:02:15] of a more near specific way so I'm gonna
[01:02:18] stop there I'm 20 minutes over time
[01:02:21] already
[01:02:22] I warned you guys not to ask me
[01:02:23] questions about science any questions
[01:02:29] otherwise I mean maybe please send me
[01:02:38] emails or comments you know I'm happy to
[01:02:40] answer questions look at the tool box
[01:02:42] first in terms of the demo folders
[01:02:45] because pretty much anytime someone has
[01:02:48] a speed a hey that would be cool to show
[01:02:51] people I've written a demo for it and
[01:02:53] shoved it in the toe box and they're all
[01:02:55] pretty descriptive like there's one
[01:02:57] called example of how to load
[01:02:59] Vina yeah it's it's it's I try to name
[01:03:02] them very descriptive things but
[01:03:06] otherwise thank you